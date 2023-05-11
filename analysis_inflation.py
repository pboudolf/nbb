import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = "https://raw.githubusercontent.com/pboudolf/nbb/main/inflation_and_hicp.csv"
df = pd.read_csv(url)

# Clean the dataset by removing any missing values
df.dropna(inplace=True)

# Convert the date column to a datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Plot the inflation rate and HICP for the EU and EA over time
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

axes[0].plot(df['Date'], df['Inflation EU'], label='EU')
axes[0].plot(df['Date'], df['Inflation EA'], label='EA')
axes[0].set_ylabel('Inflation rate')
axes[0].legend()

axes[1].plot(df['Date'], df['HICP EU'], label='EU')
axes[1].plot(df['Date'], df['HICP EA'], label='EA')
axes[1].set_ylabel('HICP')
axes[1].legend()

plt.show()

