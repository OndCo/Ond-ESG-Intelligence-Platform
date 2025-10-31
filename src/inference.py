import pandas as pd
from tensorflow.keras.models import load_model

# 1️⃣ Load your trained model
model = load_model("model/esg_total_score_model.keras")

# 2️⃣ Load the dataset used for training
df = pd.read_csv("rawdata/data.csv")

# 3️⃣ Select the feature columns your model was trained on
feature_columns = ["carbon_emission", "water_usage", "energy_consumption", "governance_score"]
X_test = df[feature_columns]

# 4️⃣ Make predictions
predictions = model.predict(X_test)

# 5️⃣ Add predictions to your dataframe
df["predicted_esg_score"] = predictions

# 6️⃣ Save the predictions to a new CSV
df.to_csv("predictions.csv", index=False)

print("Predictions saved to predictions.csv")
