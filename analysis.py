import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gross_value_by_activity.csv")

print(df.head())

#Get number of unique activities
print(df['Industry Breakdown'].nunique())

#Plot the GVA by activity over time
pivot = df.pivot_table(index='year', columns='activity', values='gva', aggfunc='sum')
pivot.plot(figsize=(12, 8))
plt.ylabel('GVA (millions of euros)')
plt.title('GVA by Economic Activity in Belgium')
plt.show()

#Get GDP of 2019
gva_by_year = df.groupby('year')['gva'].sum()

gdp_2019 = gva_by_year[2019]
print(gdp_2019)
