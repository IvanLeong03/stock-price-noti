
import time
import datetime
import yfinance as yf

STOCK = '0700.HK'
TARGET_PRICE = 550

while True:
    stock = yf.Ticker(STOCK)
    price = stock.history(period='1d')['Close'].iloc[-1]
    print(f'Current price: {price}')
    
    print(f'Current date/time: {datetime.datetime.now()}')
    time.sleep(60)