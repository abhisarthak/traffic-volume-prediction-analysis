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

## Project Structure

- `week1_project.ipynb` → Complete notebook
- `Week1_Traffic_Report_Abhishek.docx` → Detailed report
- `images/` → Project screenshots and graphs

---

## Future Improvements
- Add lag features
- Try XGBoost models
- Deploy using Streamlit
- Build real-time traffic dashboard

---

## Author
Abhishek Kumar
IIT Kharagpur
