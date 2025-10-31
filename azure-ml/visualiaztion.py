import matplotlib.pyplot as plt

# Take top 10 companies
top10 = results_df.head(10)

# Plot bar chart
plt.figure(figsize=(12,6))
plt.bar(top10["ticker"], top10["Predicted_Total_Score"], color="skyblue")
plt.xlabel("Company Ticker")
plt.ylabel("Predicted ESG Total Score")
plt.title("Top 10 Companies by Predicted ESG Total Score")
plt.xticks(rotation=45)
plt.show()
