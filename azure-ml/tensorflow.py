import tensorflow as tf

# Simple regression model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=[X_train.shape[1]]),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)  # regression output
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, validation_split=0.2)



## Step 5: Evaluate predictions

loss, mae = model.evaluate(X_test, y_test)
print(f"Test MAE: {mae}")

predictions = model.predict(X_test)
predictions[:5]  # view first 5 predictions



# Save locally in your compute instance

model.save("esg_forecast_model")

