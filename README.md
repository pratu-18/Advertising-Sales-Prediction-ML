# ADVERTISING SALES PREDICTION USING MULTIPLE LINEAR REGRESSION

1. PROJECT DESCRIPTION

---

This project implements a Multiple Linear Regression Machine Learning model
to predict product sales based on advertising expenditure across different
media channels.

The model uses the following independent variables:

* TV advertising
* Radio advertising
* Newspaper advertising

The dependent variable is:

* Sales

The project follows a complete Machine Learning workflow including data
loading, exploratory data analysis, correlation analysis, feature selection,
train-test splitting, model training, prediction, model evaluation, and
coefficient analysis.

2. PROJECT OBJECTIVE

---

The main objective of this project is to build a Multiple Linear Regression
model that predicts sales based on advertising expenditure.

The project also demonstrates how different advertising channels contribute
to the predicted sales value through regression coefficients.

3. DATASET

---

Dataset file:

Advertising.csv

The dataset contains advertising expenditure and corresponding sales data.

Input features:

1. TV
2. radio
3. newspaper

Target variable:

sales

4. MACHINE LEARNING ALGORITHM

---

Algorithm:

Multiple Linear Regression

Implementation:

LinearRegression from Scikit-learn

The regression model represents the relationship between the input features
and sales using the equation:

sales = b0 + b1(TV) + b2(radio) + b3(newspaper)

Where:

b0 = Intercept

b1 = TV coefficient

b2 = Radio coefficient

b3 = Newspaper coefficient

5. TECHNOLOGIES USED

---

Programming Language:

Python 3.10 or higher

Development Environment:

Visual Studio Code

Libraries:

* Pandas
* NumPy
* Matplotlib
* Scikit-learn

6. PROJECT WORKFLOW

---

Step 1: Load the Dataset

The Advertising.csv dataset is loaded using Pandas.

Function used:

pd.read_csv()

Step 2: Remove Unwanted Columns

The program checks whether the dataset contains the automatically generated
column:

Unnamed: 0

If present, the column is removed because it is not required for model
training.

Step 3: Check Missing Values

The project checks every column for missing values using:

df.isnull().sum()

This helps ensure that the dataset does not contain unexpected missing
values before model training.

Step 4: Statistical Summary

The describe() function is used to generate statistical information about
the dataset.

The summary includes:

* Count
* Mean
* Standard deviation
* Minimum
* 25th percentile
* Median
* 75th percentile
* Maximum

Step 5: Correlation Analysis

The project calculates the correlation between the numerical variables using:

df.corr()

Correlation analysis helps understand the relationship between advertising
features and sales.

Step 6: Feature and Target Selection

Independent variables:

TV
radio
newspaper

Dependent variable:

sales

The independent variables are stored in X and the dependent variable is
stored in Y.

Step 7: Train-Test Split

The dataset is divided into training and testing datasets.

Configuration:

test_size = 0.2
random_state = 42

80 percent of the data is used for training and 20 percent is used for
testing.

Step 8: Create and Train the Model

A Multiple Linear Regression model is created using:

LinearRegression()

The model is trained using:

model.fit(X_train, Y_train)

Step 9: Test the Model

The trained model predicts sales values for the test dataset using:

model.predict(X_test)

Step 10: Evaluate the Model

The following evaluation metrics are calculated:

* Mean Squared Error
* Root Mean Squared Error
* R2 Score

Step 11: Display Regression Coefficients

The model coefficients are displayed for:

* TV
* Radio
* Newspaper

The intercept is also displayed.

7. MODEL EVALUATION

---

Mean Squared Error:

MSE measures the average squared difference between the actual and predicted
sales values.

Lower MSE generally indicates better prediction performance.

Root Mean Squared Error:

RMSE is the square root of MSE.

It represents prediction error in the same unit as the target variable.

Lower RMSE generally indicates better model performance.

R2 SCORE:

R2 measures how well the independent variables explain the variation in the
dependent variable.

A value closer to 1 generally indicates a better fit.

8. REGRESSION COEFFICIENTS

---

The model generates one coefficient for each advertising feature.

TV coefficient:

Represents the estimated change in sales associated with a one-unit change
in TV advertising expenditure, while keeping the other variables constant.

Radio coefficient:

Represents the estimated change in sales associated with a one-unit change
in radio advertising expenditure, while keeping the other variables constant.

Newspaper coefficient:

Represents the estimated change in sales associated with a one-unit change
in newspaper advertising expenditure, while keeping the other variables
constant.

Intercept:

Represents the estimated sales value when all input features are zero.

9. PROJECT STRUCTURE

---

Advertising-Sales-Prediction-ML/
|
|-- Advertising.csv
|-- advertising_sales_prediction.py
|-- README.txt
|-- requirements.txt

10. INSTALLATION

---

Requirement:

Python 3.10 or higher

Check Python version:

python --version

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install project dependencies:

pip install -r requirements.txt

11. EXECUTION

---

Open the project folder in Visual Studio Code.

Run the program using:

python advertising_sales_prediction.py

12. EXPECTED OUTPUT

---

The program displays:

* Initial dataset records
* Cleaned dataset
* Missing value information
* Statistical summary
* Correlation matrix
* Independent variables
* Dependent variable
* Training dataset shape
* Testing dataset shape
* Model training confirmation
* Actual test values
* Predicted test values
* MSE
* RMSE
* R2 score
* TV coefficient
* Radio coefficient
* Newspaper coefficient
* Model intercept

13. KEY CONCEPTS IMPLEMENTED

---

This project demonstrates practical knowledge of:

* Python
* Pandas
* NumPy
* Data preprocessing
* Exploratory Data Analysis
* Missing value checking
* Statistical analysis
* Correlation analysis
* Feature selection
* Train-test splitting
* Multiple Linear Regression
* Model training
* Model prediction
* Mean Squared Error
* Root Mean Squared Error
* R2 Score
* Regression coefficients
* Model interpretation

14. LEARNING OUTCOMES

---

After completing this project, the following concepts are demonstrated:

* Understanding Multiple Linear Regression
* Preparing data for Machine Learning
* Selecting independent and dependent variables
* Splitting data into training and testing sets
* Training a regression model using Scikit-learn
* Making predictions using a trained model
* Evaluating regression models
* Understanding regression coefficients
* Interpreting the relationship between advertising expenditure and sales

15. FUTURE ENHANCEMENTS

---

Possible improvements include:

* Add visualization of advertising expenditure versus sales.
* Add a correlation heatmap.
* Add residual analysis.
* Compare Linear Regression with other regression algorithms.
* Perform cross-validation.
* Apply feature selection.
* Add prediction functionality for new advertising budgets.
* Save the trained model using joblib.
* Create a Streamlit application for sales prediction.
* Add automated model evaluation.

16. AUTHOR

---

Author:

Pratiksha Mahale

Project Type:

Machine Learning Regression Case Study

Algorithm:

Multiple Linear Regression

Domain:

Machine Learning and Data Science
