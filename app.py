from flask import Flask, request, jsonify, render_template
import csv
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

DATA_FILE = 'soil_data.csv'
latest_moisture_value = "Bilinmiyor"
predicted_value = "Hesaplanmadı"
recommendation = "Henüz öneri yok."

# CSV başlığı kontrolü
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['moisture_value'])


@app.route('/soil', methods=['POST'])
def soil_data():
    """Sensörden gelen nem değerini kaydeder."""
    global latest_moisture_value
    data = request.get_json()

    if not data or 'moisture' not in data:
        return jsonify({"error": "Geçersiz veri"}), 400

    moisture_value = data['moisture']
    latest_moisture_value = moisture_value

    # Veriyi dosyaya yaz
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([moisture_value])

    return jsonify({"message": "Veri kaydedildi."})


@app.route('/moisture', methods=['GET'])
def get_latest_moisture():
    """Son nem değerini döndürür."""
    if latest_moisture_value == "Bilinmiyor":
        return jsonify({"moisture": "Veri yok"})
    return jsonify({"moisture": latest_moisture_value})


@app.route('/')
def index():
    """Ana sayfa ve tahmin işlemi"""
    global predicted_value, recommendation

    try:
        df = pd.read_csv(DATA_FILE)
    except:
        return "Henüz yeterli veri yok."

    if len(df) < 2:
        return "Analiz ve tahmin için yeterli veri yok."

    # Basit regresyon tahmini
    X = np.array(range(len(df))).reshape(-1, 1)
    y = df['moisture_value'].values.reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, y)
    sonraki_index = [[len(df)]]
    predicted_value = model.predict(sonraki_index)[0][0]

    # Basit öneri kuralları
    if predicted_value < 300:
        recommendation = "Makine Öğrenimi Önerisi: Toprak çok kuru, sulama yapmalısınız."
    elif predicted_value < 700:
        recommendation = "Makine Öğrenimi Önerisi: Toprak nemi ideal."
    else:
        recommendation = "Makine Öğrenimi Önerisi: Toprak çok nemli, fazla sulamaktan kaçının."

    return render_template('index.html',
                           latest_moisture=latest_moisture_value,
                           predicted=predicted_value,
                           recommendation=recommendation)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 