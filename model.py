import joblib
import numpy as np
import os

# ---------------------------------------------------------------------------
# This must exactly match the column order your model was trained on:
# Index(['Demand', 'Stock', 'CompetitorPrice', 'CustomerRating', 'Discount',
#        'HistoricalSales', 'Distance_km', 'SurgeMultiplier',
#        'Season_Festival', 'Season_Monsoon', 'Season_Normal', 'Season_Wedding',
#        'DayTime_Late Night', 'DayTime_Midday', 'DayTime_Morning Peak',
#        'DayTime_Night'])
# ---------------------------------------------------------------------------
FEATURE_ORDER = [
    'Demand', 'Stock', 'CompetitorPrice', 'CustomerRating', 'Discount',
    'HistoricalSales', 'Distance_km', 'SurgeMultiplier',
    'Season_Festival', 'Season_Monsoon', 'Season_Normal', 'Season_Wedding',
    'DayTime_Late Night', 'DayTime_Midday', 'DayTime_Morning Peak', 'DayTime_Night',
]

SEASONS = ['Festival', 'Monsoon', 'Normal', 'Wedding']
DAY_TIMES = ['Late Night', 'Midday', 'Morning Peak', 'Night']

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')

model = None
MODEL_LOADED = False

try:
    model = joblib.load(MODEL_PATH)
    MODEL_LOADED = True
except FileNotFoundError:
    # Model file not present yet — the app will still run so you can see
    # the UI, but /predict will raise until you drop your model.pkl here.
    MODEL_LOADED = False


def predict_price(demand, stock, competitor_price, customer_rating, discount,
                   historical_sales, distance_km, surge_multiplier,
                   season, day_time):

    if not MODEL_LOADED:
        raise RuntimeError(
            "model.pkl not found. In your training notebook, run "
            "joblib.dump(rf_model, 'model.pkl') and place the file next to app.py"
        )

    if season not in SEASONS:
        raise ValueError(f"season must be one of {SEASONS}")
    if day_time not in DAY_TIMES:
        raise ValueError(f"day_time must be one of {DAY_TIMES}")

    row = {
        'Demand': demand,
        'Stock': stock,
        'CompetitorPrice': competitor_price,
        'CustomerRating': customer_rating,
        'Discount': discount,
        'HistoricalSales': historical_sales,
        'Distance_km': distance_km,
        'SurgeMultiplier': surge_multiplier,
        'Season_Festival': 1 if season == 'Festival' else 0,
        'Season_Monsoon': 1 if season == 'Monsoon' else 0,
        'Season_Normal': 1 if season == 'Normal' else 0,
        'Season_Wedding': 1 if season == 'Wedding' else 0,
        'DayTime_Late Night': 1 if day_time == 'Late Night' else 0,
        'DayTime_Midday': 1 if day_time == 'Midday' else 0,
        'DayTime_Morning Peak': 1 if day_time == 'Morning Peak' else 0,
        'DayTime_Night': 1 if day_time == 'Night' else 0,
    }

    feature_vector = np.array([[row[col] for col in FEATURE_ORDER]])
    prediction = model.predict(feature_vector)
    return float(prediction[0])
