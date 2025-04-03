# Uses all features.
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# from helpers import my_custom_regression_evaluator


# Load data set.
housing = fetch_california_housing()


# Process and view
X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = housing.target  # Median house value in $100,000s
print(f"\nFeatures df shape: {X.shape}")
print(f"\nFeatures df sample:\n{X.head()}")
print(f"\nTarget array shape: {y.shape}")
print(f"\nTarget array sample:\n{y[:5]}") 


# Split into X, y.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Scale the data.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Create model and fit it to the training data.
model = LinearRegression()
model.fit(X_train_scaled, y_train)


# Make predictions.
y_pred = model.predict(X_test_scaled)


# Calculate and print errors.
print("\nEvaluate model performance on test data:")
r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2:.4f}")

mse = mean_squared_error(y_test, y_pred)
print(f"Mean squared error: {mse:.4f}")

rmse = mse ** 0.5
print(f"Root mean squared error: {rmse:.4f}\n")


# Print coefficients.



# Custom evaluation function.
# width = 0.4
# custom_evaluation_result = my_custom_regression_evaluator(y_test, y_pred, width)
# print(f"{custom_eval_result * 100:.1f}% of predictions are within {width * 100:.1f}% of the true value.")