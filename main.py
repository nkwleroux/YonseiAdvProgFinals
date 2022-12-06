import pandas as pd
import os

from statistics import mean
import numpy as np
from sklearn.model_selection import train_test_split

# temp solution
from sklearn import linear_model

# LASSO REGRESSION() 
# 1. data ←read (‘data.csv’) 
# 2. (train_features,train_stock_price)← training_function() 
# 3. (test_features,test_stock_price)←testing_function() 
# 4. Model←LASSO_train(train_features ,train_stock_price, lambda) 
# 5. stock_price_predict← LASSO_predict(train_features) 
# 6. MAPE ← mean [abs{(test_stock_price – stock_price_predict)/test_stock_price}] * 100 
# 7. RMSE ← sqrt [mean{(test_stock_price – stock_price_predict)2}] 

# Not necessary.
def get_tickers():
    tickers = [] 

    with open('tickers.txt') as tickers_file:
        for line in tickers_file:
            tickers.append(line),

    for i in range(len(tickers)):
        tickers[i] = list(tickers[i].split(" "))
        print(tickers[i])
        
    temp_tickers = []
    for i in range(len(tickers)):
        temp_ticker = tickers[i][2].strip()
        counter = 0
        
        while(temp_ticker in temp_tickers):
            counter+=1
            temp_ticker = tickers[i][2] + "-" + str(counter)
        
        tickers[i] = temp_ticker   
        temp_tickers.append(tickers[i])    
         
    return tickers

def read_file(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return pd.read_csv(dir_path + '\\' + "csv-files" + '\\' + filename)

def get_training_and_testing_data(x, y, test_size):
    # 2. (train_features,train_stock_price)← training_function() 
    # 3. (test_features,test_stock_price)←testing_function() 
        
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    return x_train, x_test, y_train, y_test

# Not sure if im supposed to make my own model or use sklearn
def get_model(df):
     # 4. Model←LASSO_train(train_features ,train_stock_price, lambda) 

    pass

def get_stock_price_predict(model):
    # 5. stock_price_predict← LASSO_predict(train_features) 
    return model.predict()
    
def get_mape(test_stock_price, stock_price_predict):
    # 6. MAPE ← mean [abs{(test_stock_price – stock_price_predict)/test_stock_price}] * 100 

    # not entirely sure if this is correct
    # mape = mean([abs((test_stock_price[i] - stock_price_predict[i])/test_stock_price[i]) for i in range(len(test_stock_price))]) * 100
    return mean(abs((test_stock_price - stock_price_predict)/test_stock_price) ) * 100 

def get_rmse(test_stock_price, stock_price_predict):
    # 7. RMSE ← sqrt [mean{(test_stock_price – stock_price_predict)2}] 

    return np.sqrt(mean((test_stock_price - stock_price_predict)**2))
 
# trading_days = 3686
# start_date = datetime.date(1999, 4, 4)
# end_date = datetime.date(2014, 1, 3)
# training_percent = 0.7
# test_percent = 0.3
# Each of the samples composed of daily information 
# including low price, high price, opening price, close price, and trading volume
def lasso_model(ticker):
    # LASSO REGRESSION() MODEL (GS.csv)
    df = read_file(ticker + '.csv')
    print(df)
    # not sure if y should be df['Close'] or df['Volume']
    x_train, x_test, y_train, y_test = get_training_and_testing_data(df, df['Close'], 0.3) #redundant?
    # x_train, x_test, y_train, y_test = train_test_split(df, df['Close'], 0.3)
    
    #train model
    # TODO -think have to implement this my self, temporarily using skleran lasso model.
    # no clue what the aplha level is.
    clf = linear_model.Lasso(alpha=0.1)
    clf.fit(x_train, y_train) # n_sample, n_features (not sure what lambda is or how to use it)
    clf.predict(x_test) 
    
    pass


# trading_days = 734
# start_date = datetime.date(2010, 1, 4)
# end_date = datetime.date(2012, 12, 31)
# training_percent = 0.8
# test_percent = 0.2
## TODO - more than 1 model/function?
def ridge_model(ticker):
    # Ridge and a Bayesian regularized artificial neural network (GS-1.csv)
    df = read_file(ticker + '.csv')
    print(df)
    # not sure if y should be df['Close'] or df['Volume']
    # x_train, x_test, y_train, y_test = get_training_data(df, df['Close'], 0.2) #redundant?
    x_train, x_test, y_train, y_test = train_test_split(df, df['Close'], 0.2)
    
    pass

#really confused...
def trying_to_understand_formulas():
    # Consider the set of training vectors (x, ), x belongs to Rn, belongs to R,
    #1 i = 1...N
    ### number of features?
    
    # The hypothesis or the linear regression output is given by the following:
    #2 h (x) = d sigma notation (j = 0) wj xj = w^T * x
                                                #transpose of w
    n = 0 #TODO
    w = [] #TODO - weight vector
    x_train = [] #TODO
    y_train = [] #TODO

    #if x^0 = 1
    x_train[0] = 1 # I think?   

    #eq2 = h(x)
    eq2 = (w[j] * x_train[j] for j in range(len(x_train))) # = w^T * x	
    
    #eq3 = j(w)
    eq3 = (1/n) * (eq2[i] - y_train[i] for i in range(len(eq2)))**2 #this is very wrong
                                                
    # The cost function or the squared error function is defined as follows:
    #3 E (w) = 1/N * (N sigma notation (i = 0)) * (h(xi) - yi)2 = 1/N  ||Xw - y||^2 
    ## w = weight vector
    ## d = dimension of the feature vector (number of features)
    
    
    #9 E (w) = 1/N * (N sigma notation (i = 0)) * (h(xi) - yi)2 + lambda * (d sigma notation (j = 0)) ||w||^2 = 1/N ||Xw - y||^2 + lambda ||w||^2
    
    
    pass

def main():
    
    ## not necessary
    
    tickers = get_tickers()
    
    for list in tickers:
        print(list)
        # read_file('data.csv')
    
    lasso_model(tickers[0])
    
    
if __name__ == "__main__":
    main()
