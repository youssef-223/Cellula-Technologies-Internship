from django.http import HttpResponse
from django.shortcuts import render 
from datetime import datetime
import pickle
import numpy as np

def home(request):
    return render(request,"home.html")

def result(request):

    # Load the model
    with open('best_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Initialize an empty dictionary to store features
    features = {}

    # Extract and process input date
    input_date = request.POST.get('date', '')
    if input_date:
        try:
            # Convert the input date to a datetime object
            date_obj = datetime.strptime(input_date, '%Y-%m-%d')
            
            # Extract year, month, and weekday
            features['year'] = float(date_obj.year)
            features['month'] = float(date_obj.month)
            features['weekday'] = float(date_obj.weekday())  # Monday is 0, Sunday is 6
        except ValueError:
            features['year'] = None
            features['month'] = None
            features['weekday'] = None

    # Extract other features from the request
    feature_names = [
        'traffic_condition', 'pickup_longitude', 'pickup_latitude',
        'dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'jfk_dist',
        'ewr_dist', 'lga_dist', 'nyc_dist', 'distance', 'bearing'
    ]

    for feature in feature_names:
        value = request.POST.get(feature)
        if value:
            try:
                # Convert values to appropriate types
                if feature in ['traffic_condition', 'pickup_longitude', 'pickup_latitude',
                               'dropoff_longitude', 'dropoff_latitude', 'jfk_dist',
                               'ewr_dist', 'lga_dist', 'nyc_dist', 'distance', 'bearing']:
                    features[feature] = float(value)
                elif feature == 'passenger_count':
                    features[feature] = float(value)
                else:
                    features[feature] = value
            except ValueError:
                features[feature] = None
        else:
            features[feature] = None

    # Ensure the features are in the correct order expected by the model
    ordered_features = [
        features.get('traffic_condition', 0.0),
        features.get('pickup_longitude', 0.0),
        features.get('pickup_latitude', 0.0),
        features.get('dropoff_longitude', 0.0),
        features.get('dropoff_latitude', 0.0),
        features.get('passenger_count', 0.0),
        features.get('month', 0.0),
        features.get('weekday', 0.0),
        features.get('year', 0.0),
        features.get('jfk_dist', 0.0),
        features.get('ewr_dist', 0.0),
        features.get('lga_dist', 0.0),
        features.get('nyc_dist', 0.0),
        features.get('distance', 0.0),
        features.get('bearing', 0.0)
    ]

    print('*'*100)
    print()
    print('*'*100)
    # Make the prediction
    prediction = model.predict([ordered_features])

    return render(request, 'result.html', {'prediction': prediction, 'features': features})

