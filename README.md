# Traffic Volume Prediction & Analysis

## Project Overview

Traffic Volume Prediction & Analysis is a data analytics and machine learning project focused on understanding historical traffic patterns and predicting traffic volume using time-based and calendar-related features.

The project involves an end-to-end analytical workflow, starting from data cleaning and exploratory data analysis (EDA) to feature engineering, machine learning model development, evaluation, and interactive visualization.

Multiple regression models were explored to understand traffic patterns and evaluate their predictive performance. The project also incorporates SQL-based analytics using SQLite to extract meaningful insights from traffic data.

The developed solution includes an interactive Streamlit dashboard that allows users to explore traffic scenarios and obtain traffic volume predictions.

**Key Components:**
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA) and traffic pattern analysis
- Temporal and calendar-based feature engineering
- Regression model development and evaluation
- SQL-based analytics using SQLite
- Prediction error analysis
- Interactive traffic prediction dashboard

## Problem Statement

Urban traffic congestion is a major challenge for transportation systems. Traffic volume varies throughout the day and is influenced by several factors, including time of day, day of the week, month, holidays, and weather conditions.

Understanding these variations is important for identifying peak traffic periods, analysing travel patterns, and supporting better transportation planning.

The objective of this project is to analyse historical traffic data, identify the patterns and factors associated with traffic volume, and develop machine learning models capable of predicting traffic volume based on temporal and calendar-related features.

## Project Objectives

The major objectives of this project are:

1. **Data Understanding:** Examine the historical traffic dataset and understand its structure, variables, and data quality.

2. **Data Preprocessing:** Handle duplicate records, missing values, and data inconsistencies to prepare the dataset for analysis.

3. **Exploratory Data Analysis:** Identify traffic patterns across different hours, weekdays, weekends, months, holidays, and weather conditions.

4. **Feature Engineering:** Extract meaningful temporal and calendar-based features to improve the predictive capability of machine learning models.

5. **Predictive Modelling:** Develop and evaluate regression models to estimate traffic volume using historical patterns.

6. **Model Evaluation:** Compare model performance using appropriate evaluation metrics and analyse prediction errors.

7. **SQL-Based Analytics:** Use SQLite and SQL queries to perform structured data analysis and extract meaningful traffic-related insights.

8. **Interactive Visualization:** Develop a Streamlit dashboard to explore traffic scenarios and generate traffic volume predictions.

9. **Decision Support:** Translate analytical findings into insights that can support traffic monitoring and transportation planning.


## Dataset Description

The project uses historical traffic volume data containing timestamp-based observations along with weather and holiday-related information.

The dataset is used to analyse variations in traffic volume over time and develop machine learning models for traffic volume prediction.

### Dataset Overview

| Attribute | Description |
|---|---|
| Dataset file | `Train.csv` |
| Initial records | 33,750 |
| Initial columns | 15 |
| Target variable | `traffic_volume` |
| Data type | Time-series / tabular data |
| Observation frequency | Hourly traffic observations |

### Key Categories of Features

The dataset contains information belonging to the following categories:

| Feature Category | Description |
|---|---|
| Traffic Information | Historical traffic volume |
| Temporal Features | Date and time information |
| Calendar Features | Day of the week, month, and holiday information |
| Weather Features | Temperature, rainfall, snowfall, cloud coverage, and weather conditions |

### Dataset Preparation

During the initial data inspection and cleaning process:

- Identified 5,161 records associated with duplicate timestamps.
- Removed duplicate timestamp records to obtain 28,589 unique timestamp observations.
- Checked for missing values and data inconsistencies.
- Investigated missing hourly timestamps across the observation period.
- Examined anomalous weather observations before using the data for analysis.

After cleaning, the working dataset contained **28,589 records and 15 columns**.

**Note:** Missing hourly timestamps were investigated separately and were not artificially filled during this cleaning process.

## Repository Structure

The repository is organized into separate directories for data, machine learning models, visualizations, and dashboard development.

```text
traffic-volume-prediction-analysis/
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── Train.csv
│
├── images/
│   ├── Avg_traffic_by_holiday.png
│   ├── Holiday_traffic_pattern.png
│   ├── avg_error_by_hour.png
│   ├── avg_traffic_by_holiday_.png
│   ├── avg_traffic_by_hour.png
│   ├── avg_traffic_by_hour_on_holiday.png
│   ├── box_plot_by_holiday.png
│   ├── traffic_patter_by_holiday.png
│   └── traffic_vol_by_weather_types.png
│
├── models/
│   ├── model_features.pkl
│   └── traffic_prediction_model.pkl
│
├── traffic_volume_prediction.ipynb
├── traffic_volume_sql_analytics.ipynb
├── traffic_analysis_report.pdf
├── requirements.txt
├── LICENSE
└── README.md
```

### Directory and File Description

| File / Directory | Description |
|---|---|
| `data/` | Contains the traffic dataset used for analysis and model development. |
| `images/` | Stores visualizations generated during exploratory data analysis and model evaluation. |
| `models/` | Contains the serialized trained model and its required feature names. |
| `dashboard/` | Contains the Streamlit application for interactive traffic volume prediction. |
| `traffic_volume_prediction.ipynb` | Main notebook covering data preprocessing, EDA, feature engineering, model development and evaluation. |
| `traffic_volume_sql_analytics.ipynb` | Notebook demonstrating SQL-based analytics using SQLite. |
| `traffic_analysis_report.pdf` | Detailed project report documenting the analysis and findings. |
| `requirements.txt` | Lists the Python dependencies required to run the project. |
| `LICENSE` | Defines the licensing terms for the repository. |
| `README.md` | Provides project documentation and instructions. |

## Data Cleaning & Preprocessing

Before performing exploratory data analysis and developing machine learning models, the raw traffic dataset was examined and cleaned to improve data quality and consistency.

The initial dataset contained **33,750 records and 15 columns**.

### 1. Duplicate Timestamp Handling

During data inspection, 5,161 records associated with duplicate timestamps were identified.

Duplicate timestamp records were removed to maintain unique timestamp observations in the working dataset.

- Initial records: 33,750
- Duplicate timestamp records identified: 5,161
- Records after duplicate removal: 28,589

### 2. Missing Timestamp Analysis

After removing duplicate timestamps, the dataset was examined for missing hourly observations.

The analysis identified gaps in the hourly time series. These missing timestamps were investigated separately rather than automatically filling them with artificially generated traffic values.

This helped preserve the distinction between observed traffic measurements and periods for which no observations were available.

### 3. Missing Value Inspection

The dataset was checked for missing values across its columns.

The holiday-related information contained a large number of null entries. These values were examined as part of the holiday feature preparation.

### 4. Weather Data Anomaly Detection

Weather variables were examined to identify unusual or extreme observations.

An extreme rainfall value of 9831.3 was identified during the initial inspection. The rainfall data was subsequently cleaned, with the maximum reported rainfall value reduced to 55.63.

### 5. Final Dataset

After the cleaning process, the working dataset contained:

| Attribute | Value |
|---|---:|
| Initial records | 33,750 |
| Initial columns | 15 |
| Records after cleaning | 28,589 |
| Final columns | 15 |
| Duplicate timestamps remaining | 0 |

The cleaned dataset was then used for exploratory data analysis, feature engineering, and machine learning model development.
