import time
import datetime
import yfinance as yf

STOCK = '0700.HK'
TARGET_PRICE = 550

def is_market_open():
    now = datetime.datetime.now()
    market_open = now.replace(hour=1, minute=30, second=0, microsecond=0)
    market_close = now.replace(hour=8, minute=0, second=0, microsecond=0)
    return market_open <= now <= market_close

while True:
    print(f'Current date/time: {datetime.datetime.now().isoformat(sep=" ", timespec="seconds")}')
    if is_market_open():
        stock = yf.Ticker(STOCK)
        price = stock.history(period='1d')['Close'].iloc[-1]
        print(f'Current price: {price}')
        time.sleep(60)
        
    else:
        print('Market is closed.')        
        time.sleep(600)
    
    
