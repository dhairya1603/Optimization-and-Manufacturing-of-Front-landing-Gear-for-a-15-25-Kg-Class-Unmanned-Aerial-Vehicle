import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load Excel file (update path)
file_path = r"C:\Users\Dhairya D\Downloads\landing gear regression 2.xlsx"  # 🚨 Replace with actual path
data = pd.read_excel(file_path)

# Define variables (adjust indices if needed)
independent_vars = data.columns[:5]  # First 5 columns
dependent_vars = data.columns[5:12]  # Next 7 columns
powers = [-2, -1, 1, 2]  # Allowed exponents

# Feature transformation with safety checks
transformed_data = pd.DataFrame()

for var in independent_vars:
    # Check for zeros with negative exponents
    if (data[var] == 0).any() and any(p < 0 for p in powers):
        raise ValueError(
            f"Column '{var}' contains zeros - "
            "Cannot use negative exponents with zero values"
        )
    
    # Convert to float and create powered features
    float_series = data[var].astype(float)
    for p in powers:
        transformed_data[f'{var}^{p}'] = float_series ** p

# Regression analysis
results = {}
for dep_var in dependent_vars:
    model = RidgeCV(alphas=np.logspace(-3, 3, 50), cv=5)
    model.fit(transformed_data, data[dep_var])
    
    # Store performance metrics
    train_score = model.score(transformed_data, data[dep_var])
    cross_val_scores = cross_val_score(model, transformed_data, data[dep_var], cv=5)
    
    results[dep_var] = {
        'intercept': model.intercept_,
        'coefficients': dict(zip(transformed_data.columns, model.coef_)),
        'training_r2': train_score,
        'cv_r2_mean': cross_val_scores.mean(),
        'cv_r2_std': cross_val_scores.std()
    }

# Generate equations with R²-like formatting
for dep_var, params in results.items():
    equation = [f"{dep_var} = {params['intercept']:.4f}"]
    for var, coef in params['coefficients'].items():
        equation.append(f"{coef:+.4f}*{var}")
    print(" ".join(equation) + "\n")




