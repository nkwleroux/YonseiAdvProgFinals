import pandas as pd
import os

# LASSO REGRESSION() 
# 1. data ←read (‘data.csv’) 
# 2. (train_features,train_stock_price)← training_function() 
# 3. (test_features,test_stock_price)←testing_function() 
# 4. Model←LASSO_train(train_features ,train_stock_price, lambda) 
# 5. stock_price_predict← LASSO_predict(train_features) 
# 6. MAPE ← mean [abs{(test_stock_price – stock_price_predict)/test_stock_price}] * 100 
# 7. RMSE ← sqrt [mean{(test_stock_price – stock_price_predict)2}] 



def read_file(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    return pd.read_csv(dir_path + '/' + filename)

def main():
    read_file('data.csv')
    
if __name__ == "__main__":
    main()
