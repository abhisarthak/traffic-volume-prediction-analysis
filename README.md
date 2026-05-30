# Traffic Volume Prediction Analysis

## Project Overview
This project focuses on analysing and predicting traffic volume using Python and Machine Learning techniques.

The project includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Traffic pattern visualization
- Feature engineering
- Linear Regression model
- Random Forest Regressor model
- Model comparison and error analysis

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab

---

## Project Pipeline

1. Traffic Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Train-Test Split
6. Linear Regression Model Development
7. Random Forest Regression Model Development
8. Model Evaluation and Comparison
9. Traffic Volume Prediction
10. Insight Generation for Transportation Planning

---

## Dataset Features

The dataset contains:
- Traffic volume
- Hour
- Day of week
- Month
- Temperature
- Humidity
- Wind speed
- Air pollution index
- Rain and snow data
- Holiday information

---

## Machine Learning Models Used

### 1. Linear Regression
Used as the baseline prediction model.

### 2. Random Forest Regressor
Used to improve prediction accuracy using ensemble learning.

---

## Model Performance

| Model | Mean Absolute Error |
|------|------|
| Linear Regression | 1607 |
| Random Forest Regressor | 259 |

Random Forest performed significantly better than Linear Regression.

---

## Key Insights
- Traffic volume is strongly dependent on time-based features.
- Hour of the day is the most important feature.
- Weather variables contribute less compared to time variables.
- Rush hour periods are harder to predict accurately.

---
## Business Impact

Accurate traffic forecasting can help:

- Reduce urban congestion
- Improve traffic signal planning
- Support transportation infrastructure decisions
- Optimize public transport deployment
- Improve commuter experience
  ---

## Project Structure

traffic_volume_prediction.ipynb → Complete notebook

traffic_analysis_report.pdf → Detailed project report

traffic_volume_prediction_presentation.pptx → Project presentation

## Visualization Example

![Traffic Pattern](images/traffic_pattern_by_holiday.png)

---

## Future Improvements
• Add lag and rolling-window features
• Compare with XGBoost and LightGBM
• Develop Streamlit dashboard
• Real-time traffic forecasting
• Generate congestion mitigation recommendations

---

## Author
Abhishek Kumar
IIT Kharagpur
