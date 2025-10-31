import pandas as pd

# Load CSV
df = pd.read_csv("your_file_name.csv")

# Features: numeric columns only
features = ['environment_score', 'social_score', 'governance_score']  # choose relevant numeric columns

X = df[features]

# Target: total_score
y = df['total_score']

# Preview
print(X.head())
print(y.head())
