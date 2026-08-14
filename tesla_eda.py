import pandas as pd

# 1. Load
df = pd.read_csv('TSLA.csv')

# 2. Fix date type
df['Date'] = pd.to_datetime(df['Date'])

# 3. Sort by date
df = df.sort_values('Date').reset_index(drop=True)

# 4. Remove duplicates
df = df.drop_duplicates(subset=['Date'])

# 5. Logic checks
df = df[df['High'] >= df['Low']]
df = df[df['Close'] > 0]
df = df[df['Volume'] > 0]

# 6. Add useful columns
df['Year'] = df['Date'].dt.year
df['Daily_Return'] = df['Close'].pct_change()

# 7. Verify
print(df.isnull().sum())
print(df.shape)

# 8. Explore the data
print(df.info())
print(df.describe())

# 9. Price trend
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'])
plt.title('Tesla Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.savefig('tesla_stock_price.png')
plt.show()

# 10. Average closing price by year

yearly_close = df.groupby('Year')['Close'].mean()

print(yearly_close)

# 11. Average closing price by year - visualization

plt.figure(figsize=(12, 6))
plt.plot(yearly_close.index, yearly_close.values, marker='o')
plt.title('Average Tesla Closing Price by Year')
plt.xlabel('Year')
plt.ylabel('Average Closing Price')
plt.grid(True)
plt.savefig('tesla_yearly_average_price.png')
plt.show()

df.drop(columns=['Adj Close'], inplace=True)