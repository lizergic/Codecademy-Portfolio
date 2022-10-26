# Handling missing data
import pandas as pd
df = pd.read_csv('developer_dataset.csv')
print(df.columns)
print(df.count)
print(df.describe)
maxRows = df['RespondentID'].count()

print('%Missing Data:')
print((1 - df.count() / maxRows) * 100)

df.drop(['NEWJobHunt','NEWJobHuntResearch','NEWLearn'],
	axis = 1,
	inplace=True)

import seaborn as sns
import matplotlib.pyplot as plt

df[['RespondentID','Country']].groupby('Country').count()

missingData = df[['Employment','DevType']].isnull().groupby(df['Country']).sum().reset_index()

A=sns.catplot(
	data0missingData, kind="bar",
	x="Country", y="Employment",
	height = 6, aspect = 2)
B=sns.catplot(
	data=missingData, kind="bar",
	x="Country", y="DevType",
	height = 6, aspect = 2)
