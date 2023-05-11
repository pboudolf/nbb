import pandas as pd
import io
import requests

# Load data from URL
url = "https://raw.githubusercontent.com/pboudolf/nbb/main/inflation_and_hicp.csv"
content = requests.get(url).content.decode('utf-8')
df = pd.read_csv(io.StringIO(content))

# Print some basic information about the data
print("Number of rows: ", len(df))
print("Data types:\n", df.dtypes)
print("Summary statistics:\n", df.describe())