import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

csv_data = """Date,Open,High,Low,Close
10-03-16,774.25,776.065002,769.5,772.559998
10-04-16,776.030029,778.710022,772.890015,776.429993
10-05-16,779.309998,782.070007,775.650024,776.469971
10-06-16,779,780.47998,775.539978,776.859985
10-07-16,779.659973,779.659973,770.75,775.080017
"""

data = pd.read_csv(StringIO(csv_data))
data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%y')

plt.plot(data['Date'], data['Open'], label='Open', color='blue')
plt.plot(data['Date'], data['High'], label='High', color='orange')
plt.plot(data['Date'], data['Low'], label='Low', color='green')
plt.plot(data['Date'], data['Close'], label='Close', color='red')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Financial Data of Alphabet Inc. (Oct 3, 2016 - Oct 7, 2016)')
plt.legend()
plt.xticks(rotation=45)
plt.show()
