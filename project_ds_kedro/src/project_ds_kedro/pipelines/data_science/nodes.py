"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.0
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor



def func_split_data(df, test_size = 0.3, random_state = 9999):
    
    """Splits data into train and test datasets"""
    
    # Create dependent variables
    X = df.drop(columns=['FinalMandates'])
    y = df['FinalMandates']

    # Slipt data 
    X_train, X_test, y_train, y_test = train_test_split(
    df, y, test_size = test_size, random_state = random_state, stratify = y
    )
    
    return X_train, X_test, y_train, y_test


def func_fit_model(X_train, X_test, y_train, y_test):
    
    """Fits five regression models using a training dataset"""
    
    model=[LinearRegression(),SVR(),RandomForestRegressor(),GradientBoostingRegressor(),DecisionTreeRegressor()]

    for model in model:
        model.fit(X_train, y_train)
        score = model.score(X_train, y_train)
        pred=model.predict(X_test)
        print('Score of',model,'is:',score)
        print('MAE:',mean_absolute_error(y_test,pred))
        print('MSE:',mean_squared_error(y_test,pred))
        #print('RMSE:',np.sqrt(mean_squared_error(y_test,pred)))
        print('R2 score:',r2_score(y_test,pred))
        print('*'*100)
        print('\n') 
        
    return model