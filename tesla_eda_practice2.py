# tsla_eda_practice2.py
# step1 load libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

print("Libraries loaded")

# step2 load data
df = pd.read_csv("tsla.csv")

print ("Raw data loaded")
print("Rows")

step