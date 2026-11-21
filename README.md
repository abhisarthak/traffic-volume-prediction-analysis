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

## Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to identify patterns, trends, and relationships between traffic volume and different temporal, calendar, and weather-related variables.

The analysis focused on understanding traffic behaviour across different hours, days of the week, holidays, and weather conditions.

### 1. Hourly Traffic Pattern Analysis

Analysed average traffic volume across different hours of the day to identify periods of high and low traffic activity.

**Key observation:**
- Traffic volume varies significantly throughout the day.
- Traffic activity increases during commuting hours.
- The analysis identified 4 PM (16:00) as the hour with the highest average traffic volume in the SQL-based analysis.
- Traffic volume generally decreases during late-night and early-morning hours.

### 2. Weekday vs. Weekend Analysis

Compared traffic patterns across working days and weekends to understand differences in travel behaviour.

**Key observation:**
- Weekdays generally experience higher traffic volumes than weekends.
- Weekend traffic follows a different pattern from regular working days.
- These differences indicate that the day of the week is an important factor in explaining traffic variation.

### 3. Day-of-Week Analysis

Examined average traffic volume across individual days of the week.

**Key observation:**
- Thursday and Friday emerged as the busiest days in the SQL-based analysis.
- Traffic volume varies across the different days of the week.
- Weekly patterns provide useful information for understanding recurring traffic behaviour.

### 4. Holiday Traffic Analysis

Compared traffic volume on holidays and non-holidays to understand how special calendar events influence traffic patterns.

**Key observation:**
- Traffic volume is generally lower on holidays compared with regular working days.
- Holiday-related patterns differ from typical weekday traffic.
- Holiday information can therefore contribute to traffic volume prediction.

### 5. Weather-Based Traffic Analysis

Examined traffic volume across different weather conditions to investigate whether weather patterns are associated with changes in traffic activity.

The analysis included weather-related visualizations and comparisons of traffic volume across weather categories.

### EDA Summary

The exploratory analysis highlighted three important characteristics of the dataset:

1. **Temporal patterns:** Traffic volume changes considerably throughout the day.
2. **Weekly patterns:** Working days and weekends exhibit different traffic behaviour.
3. **Calendar effects:** Holidays are generally associated with lower traffic volume.

These findings motivated the development of time-based and calendar-related features for the machine learning models.

<img width="669" height="490" alt="image" src="https://github.com/user-attachments/assets/f5bdfb12-ec67-470c-a603-6c7ff37cc83e" />
Average traffic by hour

avg_traffic_by_hour.png

<img width="700" height="476" alt="image" src="https://github.com/user-attachments/assets/2acd8e18-0ab9-47d5-be8e-9c0ba7c13b76" />
Holiday and weekly patterns

Holiday_traffic_pattern.png

<img width="614" height="460" alt="image" src="https://github.com/user-attachments/assets/fd7526e2-77ff-4154-952c-abb17deb0414" />
Traffic by weather type

traffic_vol_by_weather_types.png

<img width="608" height="454" alt="image" src="https://github.com/user-attachments/assets/e1d3f6c0-9bdd-420b-9bac-b10af15475c0" />
Holiday comparison

box_plot_by_holiday.png

## Feature Engineering

Feature engineering was performed to convert raw timestamp, calendar, and weather information into meaningful variables that could help machine learning models capture traffic patterns.

The objective was to represent recurring traffic behaviour, calendar effects, and weather conditions in a structured format suitable for regression models.

### 1. Temporal Feature Extraction

The original `date_time` column was used to extract the following time-based features:

| Feature | Description |
|---|---|
| `hour` | Hour of the day (0–23) |
| `day_of_week` | Day of the week (Monday = 0, Sunday = 6) |
| `day` | Day of the month |
| `month` | Month of the year (1–12) |
| `year` | Calendar year |

These features help the model identify recurring traffic patterns across different times and dates.

### 2. Weekend and Holiday Features

Additional binary features were created to represent calendar-related traffic behaviour.

| Feature | Description |
|---|---|
| `is_weekend` | 1 if the observation falls on Saturday or Sunday; otherwise 0 |
| `is_holiday_flag` | 1 if the observation is a holiday; otherwise 0 |
| `is_working_day` | 1 if the observation is neither a weekend nor a holiday; otherwise 0 |

These features help distinguish regular working-day traffic from weekend and holiday traffic.

### 3. Cyclical Feature Encoding

Time-related variables such as hours, weekdays, and months have a cyclical nature.

For example, 23:00 and 00:00 are consecutive hours, even though their numerical values appear far apart. Similarly, December and January are adjacent months.

To represent these relationships, sine and cosine transformations were created:

- `hour_sin`, `hour_cos`
- `day_sin`, `day_cos`
- `month_sin`, `month_cos`

The transformations use the following general formulas:

\[
X_{\sin} = \sin\left(\frac{2\pi X}{P}\right)
\]

\[
X_{\cos} = \cos\left(\frac{2\pi X}{P}\right)
\]

Where:
- \(X\) represents the original time-related feature.
- \(P\) represents its cycle length (24 hours, 7 days, or 12 months).

This encoding represents cyclical relationships without introducing an artificial numerical gap between the end and beginning of a cycle.

### 4. Weather Feature Engineering

Weather-related variables were also prepared to investigate their potential contribution to traffic volume prediction.

The following derived features were created:

| Feature | Description |
|---|---|
| `temperature_c` | Temperature converted from Kelvin to Celsius |
| `is_raining` | 1 if rainfall is greater than zero; otherwise 0 |
| `low_visibility` | 1 if visibility is 3 miles or less; otherwise 0 |
| `cloud_category` | Categorizes cloud coverage as Clear, Partly Cloudy, or Overcast |

Additional weather variables, including humidity, wind speed, wind direction, visibility, rainfall, and cloud coverage, were considered during model experimentation.

### 5. Final Feature Selection

Different feature combinations were evaluated to understand the contribution of temporal and weather-related information.

The final model retained five core features:

| Feature | Role in Prediction |
|---|---|
| `hour` | Captures hourly traffic patterns |
| `day_of_week` | Captures differences across weekdays |
| `is_weekend` | Distinguishes weekday and weekend traffic |
| `month` | Captures monthly and seasonal variations |
| `is_holiday_flag` | Represents holiday-related traffic changes |

These five features were used to train the final HistGradientBoosting model and were also saved alongside the trained model for use in the Streamlit dashboard.

**Important:** Cyclical encodings and weather-derived features were explored during feature engineering and experimentation, but they were not included in the final deployed model.

The final feature set was kept compact while retaining the temporal and calendar information used by the selected model.


## Machine Learning Models & Model Development

The objective of the modelling stage was to develop a regression model capable of predicting traffic volume using historical temporal and calendar-related information.

Multiple machine learning algorithms and feature combinations were evaluated to identify a model that could capture the non-linear patterns present in traffic behaviour.

### 1. Chronological Train-Validation-Test Split

Since the dataset contains time-dependent observations, a chronological split was used instead of randomly shuffling the records.

| Dataset | Period | Observations |
|---|---|---:|
| Training | October 2012 – December 2015 | 17,491 |
| Validation | January 2016 – December 2016 | 7,838 |
| Testing | January 2017 – May 2017 | 3,260 |

The training dataset was used for model fitting, the validation dataset for model comparison and hyperparameter selection, and the test dataset for final performance evaluation.

### 2. Linear Regression — Baseline Model

Linear Regression was implemented as the initial baseline model.

It estimates traffic volume as a linear combination of the input features.

The model was trained using five temporal and calendar-related features:

- `hour`
- `day_of_week`
- `month`
- `is_weekend`
- `is_holiday_flag`

The baseline helped establish how well a simple linear relationship could explain traffic volume variations.

### 3. Random Forest Regression

Random Forest Regression was implemented to capture non-linear relationships between the input features and traffic volume.

The model combines predictions from multiple decision trees to produce a final prediction.

The following configurations were evaluated:

- Temporal features only
- Temporal and weather-related features
- Five core temporal and calendar features

The weather-based experiment included variables such as humidity, temperature, rainfall, visibility, wind speed, and wind direction.

Feature importance was also examined to understand the relative contribution of different variables.

### 4. HistGradientBoosting Regression

HistGradientBoostingRegressor was introduced to evaluate whether a boosting-based approach could improve prediction performance.

Unlike Random Forest, which combines predictions from independently trained trees, gradient boosting builds trees sequentially, with each new tree helping correct errors made by the existing ensemble.

The model was initially trained using the five core features.

Four hyperparameter configurations were evaluated by varying:

- `learning_rate`
- `max_iter`
- `max_leaf_nodes`
- `l2_regularization`

The configurations were compared using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R².

### 5. Model Comparison — Validation Results

The following table presents the validation performance of the main model experiments.

| Model | Features | MAE | RMSE | R² |
|---|---|---:|---:|---:|
| Linear Regression | Temporal | 1,564.99 | 1,783.35 | 0.1581 |
| Random Forest | Temporal | 345.43 | 547.12 | 0.9208 |
| Random Forest | Temporal + Weather | 339.99 | 558.36 | 0.9175 |
| Random Forest | Core Features | 345.45 | 547.22 | 0.9207 |
| HistGradientBoosting | Core Features | 334.95 | 538.27 | 0.9233 |

The validation results showed that tree-based ensemble models performed substantially better than the Linear Regression baseline.

HistGradientBoosting achieved the strongest overall validation performance among the initial model comparisons.

### 6. Hyperparameter Tuning

Four HistGradientBoosting configurations were evaluated using the validation dataset.

| Configuration | Learning Rate | Max Iterations | Max Leaf Nodes | L2 Regularization | MAE | RMSE | R² |
|---|---:|---:|---:|---:|---:|---:|---:|
| HGB_1 | 0.03 | 700 | 15 | 1.0 | 333.42 | 538.76 | 0.9232 |
| HGB_2 | 0.05 | 700 | 31 | 1.0 | 334.95 | 538.27 | 0.9233 |
| HGB_3 | 0.05 | 500 | 63 | 1.0 | 335.50 | 537.58 | 0.9235 |
| HGB_4 | 0.08 | 500 | 31 | 2.0 | 334.50 | 537.50 | 0.9235 |

HGB_1 achieved the lowest MAE, while HGB_4 achieved the lowest RMSE and highest R².

HGB_4 was selected as the final configuration because it provided the best RMSE and R² combination with a competitive MAE.

### 7. Final Model Training

After selecting HGB_4 using validation results, the training and validation datasets were combined to create the final training dataset.

- Final training observations: 25,329
- Final test observations: 3,260
- Number of input features: 5

The selected HistGradientBoosting model was retrained using the combined training and validation data.

The final model was then evaluated on the separate test dataset covering January to May 2017.

### 8. Final Test Performance

The final model achieved the following results:

| Evaluation Metric | Test Result |
|---|---:|
| Mean Absolute Error (MAE) | 243.72 |
| Root Mean Squared Error (RMSE) | 372.75 |
| R² Score | 0.9654 |

The final model was subsequently serialized using Joblib and saved for integration with the Streamlit dashboard.

**Selected Model:** HistGradientBoostingRegressor (HGB_4)

**Final Input Features:** `hour`, `day_of_week`, `is_weekend`, `month`, and `is_holiday_flag`.


## Model Evaluation & Error Analysis

After training the final HistGradientBoosting model, its performance was evaluated on the unseen test dataset covering January to May 2017.

In addition to evaluating overall predictive performance, error analysis was performed to understand how prediction errors varied across hours of the day, traffic periods, and day types.

### 1. Evaluation Metrics

Three regression metrics were used to evaluate the model.

| Metric | Description | Interpretation |
|---|---|---|
| MAE | Mean Absolute Error | Measures the average absolute difference between actual and predicted traffic volume. |
| RMSE | Root Mean Squared Error | Penalizes larger prediction errors more heavily than MAE. |
| R² Score | Coefficient of Determination | Measures how much of the variation in traffic volume is explained by the model. |

### 2. Overall Test Performance

The final model achieved the following performance on the test dataset:

| Metric | Result |
|---|---:|
| MAE | 243.72 |
| RMSE | 372.75 |
| R² Score | 0.9654 |

The results indicate that the model explained approximately 96.54% of the variation in traffic volume within the test dataset.

The MAE of approximately 244 means that the model's predictions differed from actual traffic volume by about 244 vehicles per observation on average.

The higher RMSE compared with MAE indicates that some observations had considerably larger prediction errors.

### 3. Residual Analysis

Residuals were calculated as:

`Residual = Actual Traffic Volume − Predicted Traffic Volume`

Residual analysis was performed to understand the direction and distribution of prediction errors.

The following statistics were obtained:

| Residual Statistic | Value |
|---|---:|
| Mean | 115.47 |
| Standard Deviation | 354.47 |
| Minimum | -3,548.88 |
| 25th Percentile | -38.79 |
| Median | 77.58 |
| 75th Percentile | 271.36 |
| Maximum | 2,460.17 |

**Key observations:**

- The positive mean residual indicates that the model underpredicted traffic volume on average.
- The positive median residual also indicates a tendency toward underprediction across the test observations.
- The negative minimum residual indicates that the model substantially overpredicted traffic volume for some observations.
- The large difference between the minimum and maximum residuals indicates that prediction errors were not uniform across all observations.

Two visualizations were used for further investigation:

- Residual distribution histogram to examine the spread and direction of errors.
- Residuals versus predicted values plot to inspect how errors varied with predicted traffic volume.

### 4. Prediction Error by Hour of the Day

The model's Mean Absolute Error was calculated separately for each hour of the day.

This analysis helped investigate whether prediction accuracy remained consistent throughout the 24-hour cycle.

An hourly error bar chart was generated to compare prediction errors across different hours.

This is useful because traffic behaviour changes considerably throughout the day, and a model may perform differently during low-traffic and high-traffic periods.

### 5. Prediction Error by Traffic Period

The test observations were grouped into four traffic periods based on the hour of the day.

| Traffic Period | Hour Range | Observations | MAE |
|---|---|---:|---:|
| Night | 00:00–05:00 and 19:00–23:00 | 1,494 | 182.47 |
| Morning Peak | 06:00–09:00 | 537 | 365.08 |
| Daytime | 10:00–15:00 | 821 | 236.65 |
| Evening Peak | 16:00–18:00 | 408 | 322.52 |

**Key observations:**

- The lowest MAE was observed during the Night period.
- The Morning Peak had the highest MAE.
- The Evening Peak also showed relatively high prediction error.
- Prediction errors were higher during peak traffic periods than during the Night period.

This suggests that predicting traffic volume during periods of heavy traffic was more challenging for the model.

### 6. Weekday vs. Weekend Prediction Performance

The test dataset was also divided into weekdays and weekends to examine whether prediction accuracy differed across day types.

| Day Type | Observations | MAE | RMSE | Average Actual Traffic |
|---|---:|---:|---:|---:|
| Weekday | 2,325 | 228.35 | 366.08 | 3,628.20 |
| Weekend | 935 | 281.95 | 388.85 | 2,757.58 |

**Key observations:**

- The model achieved lower MAE on weekdays than on weekends.
- Weekend predictions had higher MAE and RMSE.
- Average actual traffic volume was higher on weekdays than on weekends in the test dataset.

This indicates that the model's prediction accuracy varied with the type of day.

### 7. Overall Evaluation Insights

The evaluation and error analysis highlighted several important findings:

1. The final model achieved an R² score of 0.9654 on the held-out test dataset.
2. Prediction errors varied across different hours and traffic periods.
3. Peak traffic periods were more difficult to predict than the Night period.
4. Weekday predictions were more accurate than weekend predictions based on MAE and RMSE.
5. Residual analysis showed a tendency toward underprediction on average, alongside some substantial individual prediction errors.

These findings provide a more complete understanding of model performance than relying on overall evaluation metrics alone.

## SQL-Based Traffic Analytics

In addition to machine learning, SQL was used to perform structured analysis of historical traffic data.

SQLite was integrated with Python to store the traffic dataset in a relational table, execute SQL queries, and extract analytical summaries.

### 1. SQLite Database Integration

The original traffic dataset was loaded into Pandas and stored in an SQLite database.

The following tools were used:

- `sqlite3` to establish the SQLite database connection.
- `DataFrame.to_sql()` to transfer the dataset from Pandas into SQLite.
- `pd.read_sql_query()` to execute SQL queries and retrieve results.

The main database table was named `traffic_data`.

### 2. Basic SQL Data Exploration

SQL queries were used to examine the structure and statistical characteristics of the traffic dataset.

The analysis included:

| SQL Operation | Purpose |
|---|---|
| `SELECT` | Retrieve traffic records and selected columns |
| `COUNT()` | Count the total number of records |
| `AVG()` | Calculate average traffic volume |
| `MAX()` | Identify the maximum recorded traffic volume |
| `MIN()` | Identify the minimum recorded traffic volume |
| `GROUP BY` | Aggregate traffic observations by hour and day |
| `ORDER BY` | Sort results based on traffic volume |
| `LIMIT` | Restrict the number of returned records |

### 3. Hourly Traffic Analysis

SQL aggregation was used to calculate average traffic volume for each hour of the day.

The query grouped observations by the engineered `hour` feature and calculated the average traffic volume.

The results were sorted in descending order to identify the busiest hours.

**Key findings:**

| Rank | Hour | Average Traffic Volume |
|---:|---|---:|
| 1 | 4 PM | 5,639.65 |
| 2 | 5 PM | 5,309.77 |
| 3 | 3 PM | 5,232.13 |
| 4 | 2 PM | 4,942.55 |
| 5 | 1 PM | 4,714.20 |

The analysis identified **4 PM as the busiest hour**, with an average traffic volume of approximately 5,640 vehicles.

The hourly results were also retrieved into Pandas and visualized using Matplotlib.

### 4. Day-of-Week Traffic Analysis

Traffic volume was aggregated by the `day_of_week` feature to compare average traffic across the seven days.

The weekday numbering followed Python's convention:

- Monday = 0
- Tuesday = 1
- Wednesday = 2
- Thursday = 3
- Friday = 4
- Saturday = 5
- Sunday = 6

**Key findings:**

| Day | Average Traffic Volume |
|---|---:|
| Monday | 3,328.74 |
| Tuesday | 3,474.04 |
| Wednesday | 3,565.68 |
| Thursday | 3,616.89 |
| Friday | 3,609.75 |
| Saturday | 2,742.06 |
| Sunday | 2,337.17 |

Thursday recorded the highest average traffic volume, closely followed by Friday.

Weekend observations showed lower average traffic volume than weekday observations, with Sunday recording the lowest average.

A bar chart was generated using Matplotlib to visualize the differences across days.

### 5. Holiday-Based Traffic Analysis

SQL aggregation was also used to examine traffic volume across different holiday categories.

The query calculated:

- Average traffic volume for each holiday category.
- Number of records associated with each category.

The analysis showed that average traffic volume for the recorded holiday categories was generally lower than the average for observations labelled `None`.

For example:

| Category | Average Traffic Volume | Records |
|---|---:|---:|
| None | 3,243.18 | 33,707 |
| New Years Day | 1,331.60 | 5 |
| Independence Day | 1,044.67 | 3 |
| Labor Day | 1,035.50 | 4 |
| Thanksgiving Day | 855.40 | 5 |
| Christmas Day | 774.60 | 5 |

These results suggest that traffic volume was generally lower on the recorded holidays.

However, the holiday categories contain very few observations, so these averages should be interpreted cautiously rather than treated as conclusive evidence of holiday traffic behaviour.

### 6. SQL Summary Tables

The aggregated results were stored back into SQLite as separate summary tables:

| Table | Description |
|---|---|
| `hourly_traffic_summary` | Hourly average traffic volume |
| `day_traffic_summary` | Average traffic volume by day of the week |
| `holiday_traffic_summary` | Average traffic volume and record counts by holiday category |

This demonstrated how SQL query results can be organized into reusable analytical tables.

### 7. SQL and Python Integration

The SQL query results were retrieved into Pandas DataFrames for further analysis and visualization.

Matplotlib was used to create hourly traffic and day-of-week visualizations.

The notebook also retrieved the traffic data from SQLite back into Pandas, demonstrating the integration between SQL-based data retrieval and Python-based analysis.

### Key Insights from SQL Analytics

The SQL analysis highlighted three important traffic patterns:

1. **Evening traffic:** 4 PM recorded the highest average traffic volume.
2. **Weekly variation:** Thursday and Friday had the highest average traffic volumes, while Sunday had the lowest.
3. **Holiday variation:** Recorded holiday categories generally had lower average traffic volumes than the `None` category, although holiday sample sizes were small.

This SQL-based analysis complemented the machine learning workflow by providing interpretable summaries of historical traffic behaviour.

## Model Deployment & Interactive Streamlit Dashboard

After completing model development and evaluation, the selected HistGradientBoosting model was saved for reuse in an interactive prediction application.

The objective was to make the trained model accessible beyond the Jupyter Notebook, allowing users to explore traffic scenarios and obtain traffic volume predictions.

### 1. Model Serialization Using Joblib

The final trained model was serialized using the Joblib library.

Two separate files were saved:

| File | Purpose |
|---|---|
| `traffic_prediction_model.pkl` | Stores the trained HistGradientBoosting regression model. |
| `model_features.pkl` | Stores the exact list of input features used during model training. |

The model and feature list were saved inside the `models/` directory.

```python
import joblib
from pathlib import Path

models_dir = Path("models")
models_dir.mkdir(exist_ok=True)

joblib.dump(
    final_model,
    models_dir / "traffic_prediction_model.pkl"
)

joblib.dump(
    list(X_train_final.columns),
    models_dir / "model_features.pkl"
)
```

### 2. Why Was the Feature List Saved Separately?

The final model was trained using five specific input features:

- `hour`
- `day_of_week`
- `is_weekend`
- `month`
- `is_holiday_flag`

Saving the feature list separately helps maintain consistency between model training and prediction.

When a saved model is used later, the input data must contain the same features in the expected format and order.

This reduces the risk of prediction errors caused by inconsistent input preparation.

### 3. Interactive Dashboard

The project includes a Streamlit dashboard intended to provide an interactive interface for traffic volume prediction.

The dashboard serves as the user-facing layer of the project, connecting the saved machine learning model with an interactive application.

It allows users to explore traffic scenarios and obtain predicted traffic volume without directly executing the model-training notebook.

### 4. Technology Stack

| Technology | Role |
|---|---|
| Python | Application programming |
| Streamlit | Interactive dashboard framework |
| Scikit-learn | HistGradientBoosting regression model |
| Joblib | Saving and loading the trained model and feature list |
| Pandas | Preparing structured model input |

### 5. Running the Application

The Streamlit application can be started from the project root directory using:

```bash
python -m streamlit run dashboard/app.py
```

The application source code is located in the `dashboard/` directory.


