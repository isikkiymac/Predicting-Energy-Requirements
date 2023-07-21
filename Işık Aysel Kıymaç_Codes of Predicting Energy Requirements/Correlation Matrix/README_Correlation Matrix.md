# Correlation Matrix

Correlation Matrix with heatmap shows the relationship of the features in the dataset with each other. In this way, it can be observed which feature is more effective in the analyses performed.

## Requirements
- Python 3.X
- pandas library 
- matplotlib library
- seaborn library

## Installation
To provide the requirements, first make sure that you downloaded python 3.x and created IDE. 
Then, write the following commands to terminal to install required libraries:
    pip install pandas
    pip install matplotlib
    pip install seaborn

## Uploading Data
The dataset created from the original dataset to clean it is used, which is called **hourly_data.csv**.
CSV file used for storing the data.
    df = pd.read_csv('hourly_data.csv')

## Creating the Correlation and Heatmap
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='RdYlBu')
        Seaborn's heatmap function is created for color-coded map

## Output
A correlation matrix heatmap will be generated, representing the relationships between columns in the 'hourly_data.csv' dataset. Each cell in the heat map is color-coded which indicates the strength of the correlation.

## Note
The script can work with different datasets by changing the CSV file's content and column names. 