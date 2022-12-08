#use pip install matplotlib, yfinance, pandas

from matplotlib import ticker
import pandas as pd
import yfinance as yf
import datetime
import os

# LASSO REGRESSION() MODEL (GS.csv)
# trading_days = 3686
# start_date = datetime.date(1999, 5, 4)
# end_date = datetime.date(2014, 1, 3)
# training_percent = 0.7
# test_percent = 0.3
# Each of the samples composed of daily information 
# including low price, high price, opening price, close price, and trading volume


# Ridge and a Bayesian regularized artificial neural network (GS-1.csv)
# trading_days = 734
# start_date = datetime.date(2010, 1, 4)
# end_date = datetime.date(2012, 12, 31)
# training_percent = 0.8
# test_percent = 0.2

def stringDate_to_date(date_str):
    date_list = date_str.split("-")
    for i in range(len(date_list)):
        date_list[i] = int(date_list[i])
        
    return datetime.date(date_list[0], date_list[1], date_list[2])   

def ticker_to_csv(data, df_names):
    
    start_date = stringDate_to_date(data[0])  
    end_date = stringDate_to_date(data[1])
    company_ticker = data[2].strip()
    
    try:
        df = yf.download(
        tickers = company_ticker,
        start="{}".format(start_date), 
        end="{}".format(end_date),
        interval = "1d",
        ignore_tz = True,
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
        )
        
        temp_ticker = company_ticker
        counter = 0
        
        while(temp_ticker in df_names):
            counter+=1
            temp_ticker = company_ticker + "-" + str(counter)
        
        df["Ticker"] = company_ticker
        company_ticker = temp_ticker
        df_names.append(company_ticker)
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if(os.path.exists(dir_path + "\csv-files") == False):
            os.mkdir(dir_path + "\csv-files")
            
        if(os.path.exists(dir_path + "\csv-files\yFinance") == False):
            os.mkdir(dir_path + "\csv-files\yFinance")
                    
        df.to_csv(dir_path + "\csv-files\yFinance\{}.csv".format(company_ticker))
    except Exception:
        (df, "could not get")

def get_data():
    
    tickers = [] 

    with open('tickers.txt') as tickers_file:
        for line in tickers_file:
            tickers.append(line),

    for i in range(len(tickers)):
        tickers[i] = list(tickers[i].split(" "))
        
    df_names = []

    for data in tickers:
        ticker_to_csv(data, df_names)    
            
if __name__ == "__main__":
    get_data()