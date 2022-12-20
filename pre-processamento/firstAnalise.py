
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


base_credit=pd.read_csv('pre-processamento/credit_risk_dataset.csv')
#print(base_credit.head(10))
#print(base_credit.tail(2))
#print(base_credit.describe())


print(sns.countplot(x=base_credit['loan_status']))