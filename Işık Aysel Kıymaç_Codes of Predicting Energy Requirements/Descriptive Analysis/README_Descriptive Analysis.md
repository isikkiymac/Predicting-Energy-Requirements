# Descriptive Analysis

Descriptive analysis is a technique uesd for **data visualization**. Thanks to the data visualization, the relationships of the features can be examined. In this project, the change in energy consumption depending on time is examined. It will be explained how graphing is done with many different datasets (such as hourly, daily energy consumption).

## Requirements
- Python 3.X
- pandas library 
- matplotlib library

## Installation
To provide the requirements, first make sure that you downloaded python 3.x and created IDE. 
Then, write the following commands to terminal to install required libraries:
    pip install pandas
    pip install matplotlib

## Uploading Data
There are two types of uploading the dataset
1- CSV file:
    Make sure you have the needed **CSV file** at the same place with your python file. 

    Here is the example:
    data = pd.read_csv("hourly_data.csv")
    This example is from the graphing_hourly_data.py file. 

2- Using lists:
    If you don't have a long dataset, you can upload the dataset by creating **a list.**

    Here is the example:
    monthly_data = pd.DataFrame({
    'month': ['2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07',
              '2018-08', '2018-09', '2018-10', '2018-11', '2018-12'],
    'energy_consumption': [4259872.8, 3924540, 4137076.8, 4091198.4, 6008032.8, 6405595.2,
                           6205579.2, 6986512.8, 5969296.8, 5996572.8, 4846701.6, 5015440.8]
    })
    monthly_data['month'] = pd.to_datetime(monthly_data['month'], format='%Y-%m')

    This example is from the graphing_monthly_data.py file. 

## Graphing Data
    plt.figure(figsize=(12, 6))
    The figure size is decided to fit the dataset. 

    For plotting:
    1- CSV File,
        with the name you read the file, you can call its parameters by using the column names:
        data['date']
    2- Using lists
        with the name you define the list, you can call its parameters:
        plt.plot(monthly_data['month'], monthly_data['energy_consumption'])

## Output
The system will provide a line graph with the parameters you gave.

## Note
Different graphs have been created through idea mentioned above:
- Graph for Hourly Energy Consumption
- Graph for Daily Energy Consumption
- Graph for Monthly Energy Consumption
- Graph for Energy Consumption Based on the Hours of the Day
- Graph for Energy Consumption Based on the Days of the Week