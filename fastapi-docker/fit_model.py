import statsmodels.api as sm
import pandas as pd
import pickle
# Assuming you have a DataFrame 'data' with your data
# 'cheese' and 'coca' are the column names as strings

data = pd.read_csv('./data/credit_defaults.csv')

# Define the formula for logistic regression
dependent_variable = 'default'
formula = f'{dependent_variable} ~ income + age + loan'

# Create and fit the logistic regression model
model = sm.Logit.from_formula(formula, data=data).fit()

# Save Model
filename = 'logit_model.pkl'
pickle.dump(model, open(filename, 'wb'))