import pandas as pd
import csv
import plotly.figure_factory as pf

df = pd.read_csv('data.csv')
fig = pf.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()