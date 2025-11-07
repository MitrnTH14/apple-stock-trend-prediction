import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Download stock data
data = yf.download("AAPL", start="2023-01-01", end="2023-12-31")

# Prepare data
data["Days"] = np.arange(len(data))
X = data[["Days"]]
y = data["Close"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict future prices
prediction_length = 200  # make it longer
future_days = np.arange(len(data), len(data) + prediction_length).reshape(-1, 1)
future_prices = model.predict(future_days)
# Plot
plt.figure(figsize=(12,6))
plt.plot(data["Days"], y, label="Actual Prices")
plt.plot(future_days, future_prices, label="Predicted Trend", linestyle="--")

# Add labels and title
plt.xlabel("Days")
plt.ylabel("Stock Price (USD)")
plt.title("Apple Stock Price Prediction (Linear Regression)")

# Show legend
plt.legend()
plt.show()

