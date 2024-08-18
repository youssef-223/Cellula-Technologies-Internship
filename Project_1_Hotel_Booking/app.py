from flask import Flask, render_template, request
from datetime import datetime, timedelta
import joblib

app = Flask(__name__)

# Load the pre-trained model and scalers
model = joblib.load('model.pkl')  
scaler_standard = joblib.load('Sscaler.pkl')  
scaler_minmax = joblib.load('Mscaler.pkl')  

def calculate_nights(start_date, end_date):
    num_weekend_nights = 0
    num_week_nights = 0
    current_date = start_date
    while current_date < end_date:
        if current_date.weekday() >= 5:  # Saturday or Sunday
            num_weekend_nights += 1
        else:
            num_week_nights += 1
        current_date += timedelta(days=1)
    return num_weekend_nights, num_week_nights

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve data from the form
        num_adults = int(request.form['num_adults'])
        num_children = int(request.form['num_children'])
        car_parking_space = int(request.form['car_parking_space'])
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        avg_price = float(request.form['avg_price'])
        special_requests = int(request.form['special_requests'])
        meal_plan = request.form['meal_plan']
        room_type = request.form['room_type']
        market_segment = request.form['market_segment']
        prob_of_cancellation = int(request.form['prob_of_cancellation'])
        
        # Calculate lead time, stay duration, and night counts
        lead_time = (start_date - datetime.now()).days
        stay_duration = (end_date - start_date).days
        num_weekend_nights, num_week_nights = calculate_nights(start_date, end_date)
        reservation_month = start_date.month
        reservation_day_of_week = start_date.weekday()
        is_weekend = 1 if start_date.weekday() >= 5 else 0
        total_guests = num_adults + num_children

        # Scale lead time and average price
        lead_time_scaled = scaler_standard.transform([[lead_time]])[0][0]
        avg_price_scaled = scaler_minmax.transform([[avg_price]])[0][0]

        # Encode categorical features
        meal_plan_encoded = {
            'Meal Plan 1': 1,
            'Meal Plan 2': 2,
            'Not Selected': 0
        }.get(meal_plan, 0)

        market_segment_encoded = {
            'Complementary': 1,
            'Corporate': 2,
            'Offline': 3,
            'Online': 4
        }.get(market_segment, 0)

        room_type_encoded = {
            'Room Type 1': [1, 0, 0, 0, 0, 0, 0],
            'Room Type 2': [0, 1, 0, 0, 0, 0, 0],
            'Room Type 3': [0, 0, 1, 0, 0, 0, 0],
            'Room Type 4': [0, 0, 0, 1, 0, 0, 0],
            'Room Type 5': [0, 0, 0, 0, 1, 0, 0],
            'Room Type 6': [0, 0, 0, 0, 0, 1, 0],
            'Room Type 7': [0, 0, 0, 0, 0, 0, 1]
        }.get(room_type, [0, 0, 0, 0, 0, 0, 0])

        # Prepare input data for the model
        input_data = [
            num_adults, num_children, num_weekend_nights, num_week_nights, meal_plan_encoded,
            car_parking_space, lead_time_scaled, market_segment_encoded, prob_of_cancellation, avg_price_scaled,
            special_requests, reservation_month, reservation_day_of_week, is_weekend,
            stay_duration, total_guests
        ] + room_type_encoded
        
        # Make a prediction
        prediction = model.predict([input_data])
        result = "not canceled" if prediction[0] == 1 else "canceled"

        return render_template('result.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
