# Apple Stock Price Trend Prediction

This project analyzes the historical stock price trend of **Apple (AAPL)** and uses a **Linear Regression** model to predict the short-term future stock movement. The goal is to understand how closing prices evolve over time and visualize the projected trend.

## 📈 Project Overview
- Collected daily historical stock data using **Yahoo Finance (yfinance)**.
- Generated a sequential time index to model price variation over days.
- Trained a **Linear Regression** model to capture the trend.
- Predicted the next 30 days of price movement.
- Visualized **Actual vs Predicted** stock prices using Matplotlib.

## 🧠 Model Used
**Linear Regression (sklearn)**  
This is a baseline prediction approach to observe long-term trend direction.  
Note: Stock prices are non-linear by nature. This model does **not** capture volatility and is **not intended for trading decisions** — it is meant for educational & analytical understanding.

## 🗂️ Files
| File | Description |
|------|-------------|
| `main.py` | Core script for data download, model training, and prediction plotting. |
| `requirements.txt` | Python dependencies. |
| `plot.png` (optional) | Saved output graph of Actual vs Predicted trend. |

## 🔧 Technologies Used
- Python
- yfinance
- NumPy
- scikit-learn (Linear Regression)
- Matplotlib

## 📦 Install and Run

```bash
git clone https://github.com/MitrnTH14/apple-stock-trend-prediction.git
cd apple-stock-trend-prediction
pip install -r requirements.txt
python main.py
