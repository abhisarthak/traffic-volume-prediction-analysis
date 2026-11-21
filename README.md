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


## Project Results, Key Insights & Practical Applications

The project combines exploratory data analysis, machine learning, SQL-based analytics, and interactive visualization to understand historical traffic behaviour and predict traffic volume.

The results demonstrate how historical temporal and calendar-related information can be used to identify recurring traffic patterns and estimate traffic volume.

### 1. Final Model Performance

The selected HistGradientBoosting regression model was evaluated on a separate test dataset covering January to May 2017.

| Evaluation Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 243.72 |
| Root Mean Squared Error (RMSE) | 372.75 |
| R² Score | 0.9654 |

The model achieved an R² score of 0.9654, indicating that it explained approximately 96.54% of the variation in traffic volume in the test dataset.

The MAE of 243.72 indicates an average absolute prediction error of approximately 244 vehicles per observation.

### 2. Key Traffic Pattern Insights

The exploratory analysis and SQL-based analytics identified several recurring traffic patterns.

**Hourly Traffic Variation**

- 4 PM recorded the highest average traffic volume.
- 5 PM and 3 PM were the next busiest hours.
- Traffic volume varied considerably across the 24-hour period.

**Day-of-Week Variation**

- Thursday recorded the highest average traffic volume.
- Friday followed closely behind.
- Sunday recorded the lowest average traffic volume.
- Weekdays generally experienced higher traffic volume than weekends.

**Holiday Traffic Patterns**

- Recorded holiday categories generally showed lower average traffic volume than observations labelled `None`.
- Holiday observations were limited in number, so these results should be interpreted cautiously.

### 3. Model Error Analysis Insights

The prediction error analysis provided additional information about where the model performed well and where it faced challenges.

- The Night period had the lowest MAE at 182.47 vehicles.
- The Morning Peak period had the highest MAE at 365.08 vehicles.
- The Evening Peak period recorded an MAE of 322.52 vehicles.
- Weekend predictions had higher MAE than weekday predictions.

These findings indicate that prediction accuracy was not uniform across all traffic conditions.

In particular, peak traffic periods and weekend observations were relatively more challenging for the model.

### 4. Practical Applications

The analytical findings and prediction model could support several traffic-monitoring and planning activities.

| Application | Potential Use |
|---|---|
| Traffic Monitoring | Identify hours with historically high traffic volume. |
| Peak-Hour Planning | Understand recurring high-traffic periods and support planning around them. |
| Calendar-Based Planning | Compare expected traffic patterns across weekdays, weekends, and holidays. |
| Traffic Volume Estimation | Generate traffic volume estimates for selected time and calendar scenarios. |
| Historical Traffic Analysis | Support data-driven examination of recurring traffic patterns. |

These are potential applications of the developed analytical approach. The project does not claim that the model has been integrated into a live traffic management system.

### 5. Overall Project Outcomes

The project demonstrates an end-to-end data analytics and machine learning workflow:

1. Prepared historical traffic data through data cleaning and preprocessing.
2. Performed exploratory analysis to identify temporal, weekly, and holiday-related traffic patterns.
3. Created temporal, calendar, cyclical, and weather-derived features.
4. Compared Linear Regression, Random Forest, and HistGradientBoosting regression models.
5. Selected and evaluated a HistGradientBoosting model using a chronological train-validation-test approach.
6. Analysed prediction errors across different traffic periods and day types.
7. Used SQLite and SQL queries to generate structured traffic analytics.
8. Saved the trained model and feature list for reuse in an interactive application.

The final outcome is a reproducible analytical workflow that combines historical traffic analysis, machine learning-based prediction, SQL analytics, and an interactive application.

## Limitations & Future Improvements

Although the project achieved promising prediction performance, several limitations remain. These limitations also provide opportunities for further development.

### 1. Project Limitations

**1. Missing Historical Time Periods**

The original dataset contained gaps in its hourly observations.

After removing duplicate timestamps, 28,589 unique observations remained, compared with 40,527 expected hourly timestamps across the observation period.

This means approximately 29.46% of the expected hourly timestamps were missing.

These gaps may limit the model's ability to learn continuous traffic patterns across the entire observation period.

**2. Limited Input Features in the Final Model**

The final HistGradientBoosting model uses only five temporal and calendar-related features:

- `hour`
- `day_of_week`
- `is_weekend`
- `month`
- `is_holiday_flag`

Although weather-related features were explored, they did not consistently improve all evaluation metrics.

The final model therefore does not use weather information, recent traffic observations, or other external factors.

**3. Absence of Lag-Based Features**

The final model does not use previous traffic volume observations as input.

Features such as traffic volume one hour earlier, traffic volume on the previous day, and rolling averages could potentially provide additional information about short-term traffic behaviour.

**4. Limited Generalization Assessment**

The model was evaluated using a chronological test split from the same dataset.

Although this approach provides a more realistic evaluation than a random split for time-dependent data, the results do not establish how well the model would perform on a different road, geographical region, or independently collected traffic dataset.

**5. No Live Data Integration**

The project focuses on historical traffic analysis and scenario-based prediction.

It does not currently integrate live traffic sensor feeds or automatically update predictions using newly collected traffic observations.

### 2. Future Improvements

The following improvements could make the project more robust and useful.

**1. Add Lag and Rolling Statistical Features**

Introduce historical traffic information such as:

- Previous-hour traffic volume
- Previous-day traffic volume
- Previous-week traffic volume
- Rolling mean traffic volume
- Rolling standard deviation

These features could help the model capture short-term traffic trends and recurring traffic behaviour.

**2. Improve Feature Engineering**

Explore additional predictive variables, including:

- Public event schedules
- School and office working calendars
- Road-specific characteristics
- Weather conditions
- Seasonal and special-event indicators

The contribution of each feature category can be evaluated through controlled model comparisons.

**3. Explore Advanced Forecasting Models**

Compare the existing HistGradientBoosting model with additional approaches, such as:

- XGBoost
- LightGBM
- Random Forest with improved feature engineering
- Time-series forecasting models

The objective would be to determine whether more advanced approaches provide meaningful improvements over the existing model.

**4. Improve Validation and Generalization**

Future experiments could include:

- Expanding-window time-series cross-validation
- Evaluation across different time periods
- Testing on independently collected traffic datasets
- Performance comparison across different traffic conditions

This would provide a better understanding of model stability and generalization.

**5. Integrate Live Traffic Data**

Connect the application to a traffic data source or sensor feed to support predictions using recently observed traffic information.

This would move the project beyond historical scenario-based prediction toward a continuously updated traffic prediction system.

**6. Improve Dashboard and Deployment**

Further development could include:

- Hosting the Streamlit application online.
- Adding historical traffic trend visualizations.
- Comparing actual and predicted traffic volume.
- Displaying prediction errors over time.
- Adding automated model monitoring and periodic retraining.

### 3. Future Development Roadmap

| Priority | Improvement | Expected Benefit |
|---|---|---|
| High | Lag and rolling features | Capture recent traffic behaviour |
| High | Time-series cross-validation | Improve reliability assessment |
| Medium | Additional external features | Explore additional predictive signals |
| Medium | Advanced model comparison | Evaluate alternative algorithms |
| Medium | Dashboard enhancements | Improve analytical usability |
| Long-term | Live traffic integration | Support continuously updated predictions |
| Long-term | Model monitoring and retraining | Maintain performance as traffic patterns change |

### Conclusion

The current project establishes a foundation for historical traffic analysis and machine learning-based traffic volume prediction.

Future development will focus on incorporating historical traffic dependencies, improving validation, exploring additional predictive features, and moving toward a more dynamic prediction system.

## Installation, Dependencies & How to Run the Project

Follow the steps below to set up the project and run it locally.

### 1. Clone the Repository

Clone the GitHub repository:

```bash
git clone https://github.com/abhisarthak/traffic-volume-prediction-analysis.git
```

Navigate to the project directory:

```bash
cd traffic-volume-prediction-analysis
```

### 2. Create a Virtual Environment

Creating a virtual environment helps keep project dependencies separate from other Python projects.

```bash
python -m venv venv
```

Activate the environment.

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required packages using the repository's dependency file:

```bash
pip install -r requirements.txt
```

The main libraries used in the project include:

| Library | Purpose |
|---|---|
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations and feature engineering |
| Matplotlib | Data visualization |
| Scikit-learn | Regression models and model evaluation |
| Joblib | Model serialization and loading |
| Streamlit | Interactive dashboard application |
| SQLite3 | SQL-based data storage and analytics |

**Note:** SQLite3 is included with Python's standard library and does not normally require a separate pip installation.

### 4. Run the Machine Learning Notebook

Open Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
traffic_volume_prediction.ipynb
```

The notebook covers:

1. Data loading and preprocessing.
2. Exploratory Data Analysis.
3. Temporal and calendar-based feature engineering.
4. Regression model development.
5. Model comparison and hyperparameter tuning.
6. Final model evaluation and error analysis.
7. Saving the trained model and feature list.

Ensure that the dataset path in the notebook matches the location of `Train.csv` in your local project.

### 5. Run the SQL Analytics Notebook

Open:

```text
traffic_volume_sql_analytics.ipynb
```

This notebook demonstrates:

- Creating an SQLite database.
- Storing traffic data in a database table.
- Executing SQL aggregation queries.
- Analysing traffic patterns by hour, weekday, and holiday.
- Retrieving SQL query results into Pandas for visualization.

### 6. Run the Streamlit Dashboard

From the project root directory, execute:

```bash
python -m streamlit run dashboard/app.py
```

Streamlit will start the application and provide a local URL in the terminal.

### 7. Model Files

The project includes the following saved model artifacts:

```text
models/
│
├── traffic_prediction_model.pkl
└── model_features.pkl
```

The trained model and its corresponding feature list must be available at the paths expected by the dashboard application.

### 8. Project Execution Workflow

The overall execution flow is:

1. Install the project dependencies.
2. Load and prepare the historical traffic dataset.
3. Run the machine learning notebook to reproduce model development.
4. Run the SQL notebook to reproduce traffic analytics.
5. Use the saved model artifacts with the Streamlit application.

This setup allows users to explore the analytical workflow, reproduce the modelling experiments, and run the interactive prediction application.

## Conclusion

The Traffic Volume Prediction & Analysis project demonstrates an end-to-end application of data analytics, machine learning, and SQL to understand historical traffic patterns and predict traffic volume.

Starting with raw traffic data, the project involved data cleaning, exploratory data analysis, temporal and calendar-based feature engineering, regression modelling, model evaluation, and SQL-based analytical queries.

Multiple regression algorithms were evaluated, including Linear Regression, Random Forest, and HistGradientBoosting. The final HistGradientBoosting model achieved an MAE of **243.72**, an RMSE of **372.75**, and an R² score of **0.9654** on the held-out test dataset.

Beyond predictive modelling, the project identified meaningful historical traffic patterns, including peak-hour variations, differences between weekdays and weekends, and lower average traffic across the recorded holiday categories.

The project also demonstrates the integration of Python and SQLite for structured traffic analytics, along with model serialization for reuse in an interactive Streamlit application.

Overall, this project provided practical experience in building a complete data analytics and machine learning workflow, from raw data preparation to model evaluation and application development.

### Key Takeaways

- Developed an end-to-end traffic volume prediction workflow.
- Applied data preprocessing, exploratory analysis, and feature engineering.
- Compared multiple regression algorithms and selected a HistGradientBoosting model.
- Evaluated model performance using MAE, RMSE, and R².
- Performed residual and segment-based prediction error analysis.
- Used SQLite and SQL for structured traffic analytics.
- Saved the trained model and feature list for application-level reuse.
- Explored interactive prediction through Streamlit.

### Author

**Abhishek Kumar**

GitHub: [abhisarthak](https://github.com/abhisarthak)
