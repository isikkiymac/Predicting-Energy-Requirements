# Energy Consumption Prediction

This Python script shows how to predict energy consumption using Linear and Quadratic Regression models. It uses pandas, numpy, and scikit-learn (sklearn) libraries for data processing, imputation, scaling, and modeling.

## Requirements
- Python 3.x
- pandas library
- numpy library 
- scikit-learn library
  
## Installation
To provide the requirements, first make sure that you downloaded python 3.x and created IDE. 
Then, write the following commands to terminal to install required libraries:
    pip install pandas
    pip install numpy
    pip install scikit-learn

## Data Preprocessing
Loading the dataset from CSV file called "hourly_data.csv" by using pandas
"Temperature", "Humidity", and "energy_consumption" are the names of columns selected for modeling.
Missing values in the columns above are imputed with the mean using SimpleImputer from sklearn.

## Feature Scaling
The independent variables (Temperature and Humidity) were standardized using StandardScaler from sklearn with an average of 0 and a standard deviation of 1.

## Linear Regression Model
It creates a Linear Regression model using LinearRegression from sklearn on scaled independent variables (X) and target/ dependent variable (y).
The predicted energy consumption data by Linear regression are stored in **y_pred_linear**.

## Quadratic Regression Model
To produce quadratic regression, polynomial parameters with degree 2 are created using PolynomialFeatures from sklearn. The code creates a Linear Regression model on independent variables (X_quad) and target/ dependent variable (y).
The predicted energy consumption data by Quadratic regression are stored in **y_pred_quad**.

## Output
The predicted energy consumption data by the Linear Regression and Quadratic Regression are saved in the CSV files: called"linear_predictions.csv" and "quadratic_predictions.csv," respectively.

## Note
Linear Regression emphasizes a linear relationship between the independent and target/dependent variables, while Quadratic Regression emphasizes a quadratic relationship.