import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
history = model.fit(X_train, y_train, epochs=50, validation_split=0.2)

# EVALUATE THE MODEL

loss, mae = model.evaluate(X_test, y_test)
print(f"Test MAE: {mae}")

# Make predictions
predictions = model.predict(X_test)
predictions[:5]  # view first 5 predictions



## SAVE THE MODELL 

model.save("esg_forecast_model")



import tensorflow as tf

# Define simple regression model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)  # regression output
])

# Compile model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train model
history = model.fit(X_train, y_train, epochs=50, validation_split=0.2)


