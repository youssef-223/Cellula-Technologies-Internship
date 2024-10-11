# Hotel Booking Prediction Project

## Project Overview

This project aims to develop a machine learning model to predict hotel booking cancellations. By analyzing various features from the booking data, the model identifies patterns and factors influencing cancellations, enabling hotels to enhance their revenue management strategies and improve customer satisfaction.

## Key Components

1. **Data Collection:**  
   The project utilizes a comprehensive dataset containing information on hotel bookings, including customer demographics, booking conditions, and cancellation statuses.

2. **Exploratory Data Analysis (EDA):**  
   Visualizations and statistical analyses were performed to uncover trends, correlations, and insights related to booking behavior and cancellations.

3. **Data Preprocessing:**  
   The dataset was cleaned and transformed, addressing missing values and encoding categorical variables to ensure suitability for machine learning algorithms.

4. **Feature Engineering:**  
   New features were created to capture significant aspects of the data, enhancing the model's predictive power.

5. **Model Training:**  
   Various classification algorithms were employed, including Logistic Regression and Random Forest, to predict cancellations. Model performance was evaluated using metrics such as accuracy, precision, recall, and F1-score.

6. **Deployment:**  
   The final model was deployed as a web application, allowing users to input booking details and receive cancellation probability predictions.

## Conclusion

By leveraging machine learning techniques, this project offers valuable insights for hotel management, helping to reduce cancellation rates and optimize booking strategies.

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- Flask (for deployment)

## Installation


To run the project, clone this repository and install the required packages:

```bash
git clone https://github.com/youssef-223/Cellula-Technologies-ML-Internship.git
cd Project_1_Hotel_Booking
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your web browser and go to http://127.0.0.1:5000 to access the prediction interface.

