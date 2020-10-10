import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

class TitanicPredictor():
    def __init__(self, dataframe = None, fitmodel = False):
        
        if fitmodel:
            df_len = self.df_f.shape[0]
            self.df_f = dataframe
            self.X_train, self.Y_train = [], []
            for i in range(df_len):
                sex = self.df_f['Sex'].iloc[i]
                age = self.df_f['Age'].iloc[i]
                rel = self.df_f['Relatives'].iloc[i]
                pcl = self.df_f['Pclass'].iloc[i]
                self.X_train.append([sex, age, rel, pcl])
                self.Y_train.append(str(self.df_f['Survived'].iloc[i]))
        
            self.clf_f = LogisticRegression() 
            self.clf_f = self.clf_f.fit(self.X_train, self.Y_train)
        
        
    def predict_res(self, el):
        return self.clf_f.predict([el])[0]
    
    
    def save_model(self, filename='saved_model.sav'):
        with open(filename, 'wb') as f:
            pickle.dump(self.clf_f, f)
        
        
    def load_model(self, filename='saved_model.sav'):
        with open(filename, 'rb') as f:
            self.clf_f = pickle.load(f)  
