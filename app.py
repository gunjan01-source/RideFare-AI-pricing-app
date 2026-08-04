from flask import Flask, render_template, request, jsonify
from model import predict_price, MODEL_LOADED

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', model_loaded=MODEL_LOADED)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        result = predict_price(
            demand=float(data['demand']),
            stock=float(data['stock']),
            competitor_price=float(data['competitor_price']),
            customer_rating=float(data['customer_rating']),
            discount=float(data['discount']),
            historical_sales=float(data['historical_sales']),
            distance_km=float(data['distance_km']),
            surge_multiplier=float(data['surge_multiplier']),
            season=data['season'],
            day_time=data['day_time'],
        )

        return jsonify({'success': True, 'price': round(result, 2)})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
