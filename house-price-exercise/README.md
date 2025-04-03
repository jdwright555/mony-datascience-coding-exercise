# Installation Instructions

Install python 3.12

Create a virtual environment and install requirements.txt


# Data Scientist Explainable ML Test
## Task Overview

Your task is to extract some additional information about the performance of a simple linear regression model, reflecting the sort of questions one might encounter in a business environment.

## Requirements

There are 3 parts to this exercise:

1. (Preliminaries) Check you can install packages and run the `main.py` script.  
    - Note the output.

2. Add some code to the bottom of `main.py` to output the coefficients of the linear model created by the script:  
    - Which features are the most important for predicting house price?  
    - How do they influence price directionally?  

3. Create a function in `helpers.py` that calculates how many predictions fall within a specified interval around the true value:  
    - The function should have three arguments: `actual_values`, `predicted_values`, and `width`.  
    - It should return a single number: the percentage of predicted values that fall within the specified width.  
    - This allows us to communicate to the business, for example, that "80% of our predictions are within +/-20% of the true value."  
    - Import this function into `main.py`, leverage it, and print the value associated with the trained model.
