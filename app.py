from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Insert here your api key from open weather
API_KEY = "------------------"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Jab user browser me website kholey ga toh index.html render hogi
@app.route('/')
def home():
    # API key template me bhej rahay hain takay map layers load ho sakein
    return render_template('index.html', api_key=API_KEY)

# Yeh naya route humne HTML ko data dene ke liye banaya hai
@app.route('/api/weather')
def get_weather():
    city = request.args.get('q')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    params = {"appid": API_KEY, "units": "metric"}
    if city:
        params['q'] = city
    elif lat and lon:
        params['lat'] = lat
        params['lon'] = lon
    else:
        return jsonify({"error": "No location provided"}), 400
        
    # Python backend OpenWeatherMap se data fetch kar raha hai
    response = requests.get(WEATHER_URL, params=params)
    return jsonify(response.json()), response.status_code

@app.route('/api/forecast')
def get_forecast():
    city = request.args.get('q')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    params = {"appid": API_KEY, "units": "metric"}
    if city:
        params['q'] = city
    elif lat and lon:
        params['lat'] = lat
        params['lon'] = lon
    else:
        return jsonify({"error": "No location provided"}), 400
        
    # Python backend 5-day forecast fetch kar raha hai
    response = requests.get(FORECAST_URL, params=params)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    print("Starting Weather Flask Server at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)