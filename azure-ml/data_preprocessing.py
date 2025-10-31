import pandas as pd

# Replace with your uploaded file name
df = pd.read_csv("your_uploaded_file.csv")

# Preview data
df.head()


import pandas as pd

# Load your CSV
df = pd.read_csv("your_file_name.csv")

# Preview data
df.head()

# Set the target column (choose one)
target_column = "total_grade"  # or "total_level"


# Features = all columns except the target
X = df.drop(columns=[target_column])
y = df[target_column]

# Split into train and test sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
