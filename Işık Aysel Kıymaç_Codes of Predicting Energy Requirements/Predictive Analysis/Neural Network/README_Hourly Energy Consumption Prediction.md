# Hourly Energy Consumption Prediction by Neural Network

This repository has code to predict hourly energy consumption using a neural network based on actual data. The code uses Python, pandas, numpy, and TensorFlow to preprocess the data, construct the neural network model, and evaluate its performance.

## Requirements
- Python 3.x
- pandas library
- numpy library 
- scikit-learn library
- TensorFlow library
- matplotlib library

## Installation
To provide the requirements, first make sure that you downloaded python 3.x and created IDE 
Then, write the following commands to the terminal to install the required libraries:
    pip install pandas numpy scikit-learn tensorflow matplotlib

## Data Preprocessing
Loading the dataset from a CSV file called "hourly_data.csv" by using pandas
Filling missing values by using "mean"
Scaling the data to a range between 0 and 1 by using min-max scaling
Creating windowed data for sequence modeling in order to perform prediction

## Model Training and Evaluation
Data is split into training and testing sets
Building a neural network model
Compilation of the model
Training the model
Saving the best points of the model
Loading the best model to evaluate it on test data

## Data Visualization
Loading necessary libraries for data visualization
Creating mean squared error and mean absolute error to plot the errors

## Output
Hourly energy consumption predictions created by Neural Network
Graph of comparison between actual data and predicted data