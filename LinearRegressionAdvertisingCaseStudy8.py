import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error ,r2_score#it is like to calculate accuracy

def MarvellousRegression(Datapath):
    
    
    #step 1 : load the data 
    
    Border="-"*80
    print(Border)
    print("step 1 : load the data ")
    print(Border)
    
    df=pd.read_csv(Datapath)
    print(df.head()) 
    
    #step 2:Remove anwanted column
    print(Border)
    print("step 2:Remove anwanted column(EDA)")
    print(Border)
    
    if "Unnamed: 0" in df.columns:
        df=df.drop(columns=["Unnamed: 0"])
    print(df.head())   
    
    #Step 3: check missing values
    
    print(Border)
    print("Step 3: check missing values(EDA)") 
    print(Border)
    
    print("Total missing values :")
    print(Border)
    print(df.isnull().sum())
    print(Border)
    
    #Step : 4 Statistical summary
    print(Border)
    print("Step : 4 Statistical summary")
    print(Border)
    
    print(df.describe())
    
    
    #step : 5 Corelation
    
    print(Border)
    print("step : 5 Corelation")
    print(Border)
    
    print(df.corr())
    
    #Step 6 : Separate independent and dependent variables
    
    print(Border)
    print("Step 6 : Separate independent and dependent variables")
    print(Border)
    
    X=df[["TV", "radio","newspaper"]]
    Y=df["sales"]
    
    print("Independent Variales :")
    print(X.head())
    
    print("dependent Variales :")
    print(Y.head())
    
    
    print(Border)
    print("Step 7: split data")
    print(Border)
    X_train,X_test,Y_tran,Y_test=train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )
    
    print("Training Data :",X_train.shape)
    print("Testing Data :",X_test.shape)

    print(Border)
    print("Step 8 : Create and train model")
    print(Border)
    
    model=LinearRegression()
    model=model.fit(X_train,Y_tran)
    print("Model trained succesfully")
    
    
    #step :9 test the model
    print(Border)
    print("step :9 test the model")
    print(Border)
    
    Y_pred=model.predict(X_test)
    print("Expected ans: ")
    print(Y_test[:3])
    
    print("Predicted ans :")
    print(Y_pred[:3])
   
   
   #step 10 : Evaluate the model
    print(Border)
    print("step 10 : Evaluate the model")
    print(Border)
    
    MSE=mean_squared_error(Y_test,Y_pred)#like accuracy
    RMSE=np.sqrt(MSE)           #under root of MSE
    
    R2=r2_score(Y_test,Y_pred)
    print("MSE :",MSE)
    print("RMSE :",RMSE)
    print("R2 :",R2)
    
    #Step 11 : Display coeficient
    print(Border)
    print("Step 11 : Display coeficient")
    print(Border)    
    
    print("TV coeficient :",model.coef_[0]) #0 for TV
    print("Radio coeficient :",model.coef_[1])
    print("Newpaper coeficient :",model.coef_[2])
    
    print("Intercept :",model.intercept_)
    
    
def main():
    MarvellousRegression("Advertising.csv")
    
    
    
    
if __name__=="__main__":
    main()