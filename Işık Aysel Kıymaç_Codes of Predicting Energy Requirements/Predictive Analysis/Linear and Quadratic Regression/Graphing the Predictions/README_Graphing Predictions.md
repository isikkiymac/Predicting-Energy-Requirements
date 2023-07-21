# Data Visualization

Thanks to the data visualization, the relationships of the features can be examined. In this project, the change in energy consumption depending on time is examined. It will be explained how graphing is done with many different datasets. Also, different datasets will me compared with the help of mean absolute error and mean squared error.

## Requirements
- Python 3.X
- pandas library 
- matplotlib library
- numpy library
- scikit-learn library for sklearn.metrics

## Installation
To provide the requirements, first make sure that you downloaded python 3.x and created IDE. 
Then, write the following commands to terminal to install required libraries:
    pip install pandas
    pip install matplotlib
    pip install numpy
    pip install scikit-learn

## Uploading Data
Make sure you have the needed **CSV file** at the same place with your python file. 
There are two types of uploading the dataset
1- Graphing the Dataset
    Here is the example:
    data = pd.read_csv("hourly_data.csv")
    This example is from the graphing_hourly_data.py file. 
2- Comparing the Dataset
    Here is the example:
    data1 = pd.read_csv('linear_regression_analysis - Sheet1.csv')  
    data2 = pd.read_csv('hourly_data.csv')  
    This example is from the linear_regr_wtih_mse_and_mae.py file. 

## Graphing Data
plt.figure(figsize=(12, 6))
The figure size is decided to fit the dataset. 

    For plotting:
    1- Graphing the Dataset
        with the name you read the file, you can call its parameters by using the column names:
        data['date']
    2- Comparing the Dataset
        x1 = data1['Date']
        y1 = data1['energy_consumption']
        x2 = data2['Date']
        y2 = data2['energy_consumption']

        y1 = y1.fillna(y1.mean())  # filling the missing values by using "mean" technique
        y2 = y2.fillna(y2.mean())  # filling the missing values by using "mean" technique
        
        plt.plot(x1, y1, label='Linear Regression')
        plt.plot(x2, y2, label='Hourly Energy Consumption')
        This example is from the linear_regr_wtih_mse_and_mae.py file. 

## Calculating the Errors
Make sure to use correct mathematical operations for errors
#mean squared error
mse = np.mean((y1 - y2) ** 2)
mse_annotation = f'MSE: {mse:.4f}'

#mean absolute error
mae = mean_absolute_error(y1, y2)
plt.text(0.5, 0.9, f'MAE: {mae:.4f}', transform=plt.gca().transAxes)
plt.annotate(mse_annotation, (0.5, 0.95), xycoords='axes fraction')

This example is from the linear_regr_wtih_mse_and_mae.py file. 

## Output
The system will provide a line graph with the parameters you gave. If you include the error, it will dislapy the errors at the top of the line graph.

## Note
Different graphs have been created through idea mentioned above:
- Graph for Energy Consumption by Linear Regression
- Graph for Energy Consumption by Quadratic Regression
- Graph for Comparison of Actual Data and Predicted Data by Linear Regression
- Graph for Comparison of Actual Data and Predicted Data by Quadratic Regression
- Graph for Comparison of Actual Data and Predicted Data by Neural Network
- Graph for Comparison of Predicted Data by Quadratic Regressio and Predicted Data by Linear Regression