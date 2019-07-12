import yfinance as yf
import matplotlib.pyplot as plt
import ruptures as rpt

msft = yf.Ticker("SPY")

data = yf.download('spy', start= '2019-01-01', end='2019-07-11')
data = data['Close']

algo = rpt.Pelt(model='rbf').fit(data)
result = algo.predict(pen=10)

rpt.display(data, result=result)
plt.show()