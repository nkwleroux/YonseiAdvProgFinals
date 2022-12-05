#use pip install matplotlib, yfinance, pandas

from matplotlib import ticker
import pandas as pd
import yfinance as yf
import datetime
import os

# LASSO REGRESSION() MODEL (GS.csv)
# trading_days = 3686
# start_date = datetime.date(1999, 4, 4)
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

def string_to_list(string):
    listRes = list(string.split(" "))
    return listRes

def ticker_to_csv(list, df_names):
    
    start_date = stringDate_to_date(list[0])  
    end_date = stringDate_to_date(list[1])
    company_ticker = list[2].strip()
    
    try:
        
        ticker = yf.Ticker(company_ticker)
        
        df = ticker.history(start="{}".format(start_date), end="{}".format(end_date), interval='1d', auto_adjust=True)
        
        temp_ticker = company_ticker
        counter = 0
        
        while(temp_ticker in df_names):
            counter+=1
            temp_ticker = company_ticker + "-" + str(counter)
        
        company_ticker = temp_ticker
        df_names.append(company_ticker)
        df["Ticker"] = company_ticker
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if(os.path.exists(dir_path + "\csv-files") == False):
            os.mkdir(dir_path + "\csv-files")
                    
        df.to_csv(dir_path + "\csv-files\{}.csv".format(company_ticker))
    except Exception:
        (df, "could not get")

def get_data():
    
    tickers = [] 

    with open('tickers.txt') as tickers_file:
        for line in tickers_file:
            tickers.append(line),

    for i in range(len(tickers)):
        tickers[i] = string_to_list(tickers[i])

    ## redundant code
    # for i in range(len(tickers)):
    #     tickers[i] = tickers[i][:3]
        
    df_names = []

    for list in tickers:
        ticker_to_csv(list, df_names)    
            
if __name__ == "__main__":
    get_data()