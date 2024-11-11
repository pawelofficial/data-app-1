import os
import yfinance as yf

# Define parameters
tickers = ["AAPL", "MSFT", "GOOGL", "TSLA"]  # List of tickers to download
start_date = "2022-01-01"
end_date = "2022-12-31"
output_folder = "seeds/data"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for ticker in tickers:
    # Download data using yfinance
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Select only the required columns
    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    # set column names 
    data.columns = ['open', 'high', 'low', 'close', 'volume']
    # set index as a Date column 
    data['Date'] = data.index
    # reset index 
    data.reset_index(drop=True, inplace=True)
    # set column names to lowercase 
    data.columns = [col.lower() for col in data.columns]
    
    # Define the output CSV file path
    output_file_path = os.path.join(output_folder, f"{ticker}.csv")
    
    # Save data to CSV
    data.to_csv(output_file_path, index=False)
    print(f"Data for {ticker} saved to {output_file_path}")

if __name__ == "__main__":
    # Define parameters
    tickers = ["AAPL", "MSFT", "GOOGL", "TSLA"]  # List of tickers to download
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    output_folder = "output_data"