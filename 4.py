import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

ticker = "GOOGL"
start_date = "2022-01-01"
end_date = "2023-01-01"

stock_data = yf.download(ticker, start=start_date, end=end_date)

if stock_data.empty:
    print("No data available for the specified date range.")
else:
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, stock_data['Close'], label="Close Price", color='blue', linewidth=2)
    plt.title(f"Alphabet Inc. Stock Prices ({start_date} to {end_date})", fontsize=16)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Close Price (USD)", fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
