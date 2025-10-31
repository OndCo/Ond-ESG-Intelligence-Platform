from tensorflow.keras.models import load_model

# Load your saved model
model = load_model("esg_total_score_model.keras")

# Predict on the test set
predictions = model.predict(X_test)
predictions[:5]


## deploy

import pandas as pd

# Load new data
new_df = pd.read_csv("new_esg_data.csv")

# Use same features as model training
X_new = new_df[['environment_score', 'social_score', 'governance_score']]

# Make predictions
predictions = model.predict(X_new)
new_df['predicted_total_score'] = predictions
new_df.head()


from azureml.core import Workspace, Model

ws = Workspace.from_config()

# Register model in Azure ML
model_azure = Model.register(
    workspace=ws,
    model_path="esg_total_score_model.keras",
    model_name="esg_total_score_model"
)



# plot predicted vs actual 
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.scatter(results["Actual_Total_Score"], results["Predicted_Total_Score"], color='blue', alpha=0.6)
plt.plot([results["Actual_Total_Score"].min(), results["Actual_Total_Score"].max()],
         [results["Actual_Total_Score"].min(), results["Actual_Total_Score"].max()],
         color='red', linewidth=2)  # perfect prediction line
plt.xlabel("Actual Total Score")
plt.ylabel("Predicted Total Score")
plt.title("Predicted vs Actual Total Score")
plt.grid(True)
plt.show()


#Step 1: Merge predictions with company info

(assuming your test_df still has company names)

# Add predictions to the test DataFrame
test_df["Predicted_Total_Score"] = predictions.flatten()

# Show top rows
test_df.head()

#Step 2: Find the company with the highest predicted score
highest_company = test_df.loc[test_df["Predicted_Total_Score"].idxmax()]
print("Company with highest predicted ESG score:")
print(highest_company)


## predticion for all companies

# Use the full dataset (not just test split)
X_full = df[["environment_score", "social_score", "governance_score"]]
tickers_full = df["ticker"]

# Predict total score for all companies
predictions_full = model.predict(X_full)

# Build DataFrame with results
results_df = pd.DataFrame({
    "ticker": tickers_full,
    "Predicted_Total_Score": predictions_full.flatten()
})

# Sort by predicted score (highest first)
results_df = results_df.sort_values(by="Predicted_Total_Score", ascending=False)

# Show top 10 companies
print(results_df.head(10))
