# Electricity Consumption Prediction using Linear Regression

The dataset used in this project was obtained from Kaggle. Due to dataset licensing/redistribution restrictions, the original dataset is not included in this repository.

## Project Overview

A beginner machine learning project focused on predicting daily electricity consumption using Linear Regression.

## Objectives

- Explore electricity consumption data
- Perform Exploratory Data Analysis (EDA)
- Engineer meaningful features
- Understand relationships between weather, seasonality, and electricity consumption
- Build a Linear Regression model
- Evaluate model performance

## Feature Engineering

The project includes several feature engineering techniques to improve the model's ability to capture patterns in electricity consumption:

- Cyclical month features (`month_sin`, `month_cos`) to represent seasonal patterns
- Cyclical day features (`day_sin`, `day_cos`) to represent patterns across the days
- `previous_day_consumption` to incorporate the relationship between the previous day's and current day's electricity consumption

## Final Model

The final Linear Regression model uses the following five features:
TMAX
TMIN
month_sin
month_cos
previous_day_consumption

```

## Results

| Metric | Final Result |
| ------ | -----------: |
| MAE    |       274.75 |
| MSE    |   139,022.65 |
| RMSE   |       372.86 |
| R²     |   **0.3647** |

## Conclusion
This project helped me understand the complete workflow of building a Linear Regression model, from EDA and feature engineering to model training and evaluation.
Through experimentation with different features, I learned that selecting meaningful features can improve model performance and that adding more features does not always produce better results.
```
