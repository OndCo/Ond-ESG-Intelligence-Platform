import os
os.getcwd()


## importing


import pandas as pd

df = pd.read_csv("data.csv")  # replace with your actual CSV name
df.head()


## 
import pandas as pd

df = pd.read_csv("data.csv")  # exact file name from Explorer
df.head()

## Azure ML Datasets

from azureml.core import Workspace, Dataset

ws = Workspace.from_config()
dataset = Dataset.get_by_name(ws, name='esg_transformed_data')
df = dataset.to_pandas_dataframe()
df.head()

