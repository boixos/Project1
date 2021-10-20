%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv('https://raw.githubusercontent.com/boixos/Project1/master/football_data.csv?token=AQ2O445M436VV5RY5L7I2BLBJ4J6W')
data.head()

def data_clean():
    data['ShortPassing'].fillna(data['ShortPassing'].mean(), inplace = True)
    data['Volleys'].fillna(data['Volleys'].mean(), inplace = True)
    data['Dribbling'].fillna(data['Dribbling'].mean(), inplace = True)
    data['Curve'].fillna(data['Curve'].mean(), inplace = True)
    data['FKAccuracy'].fillna(data['FKAccuracy'], inplace = True)
    data['LongPassing'].fillna(data['LongPassing'].mean(), inplace = True)
    data['BallControl'].fillna(data['BallControl'].mean(), inplace = True)
    data['HeadingAccuracy'].fillna(data['HeadingAccuracy'].mean(), inplace = True)
    data['Finishing'].fillna(data['Finishing'].mean(), inplace = True)
    data['Crossing'].fillna(data['Crossing'].mean(), inplace = True)
    data['Weight'].fillna('200lbs', inplace = True)
    data['Contract Valid Until'].fillna(2019, inplace = True)
    data['Height'].fillna("5'11", inplace = True)
    data['Loaned From'].fillna('None', inplace = True)
    data['Joined'].fillna('Jul 1, 2018', inplace = True)
    data['Jersey Number'].fillna(8, inplace = True)
    data['Body Type'].fillna('Normal', inplace = True)
    data['Position'].fillna('ST', inplace = True)
    data['Club'].fillna('No Club', inplace = True)
    data['Work Rate'].fillna('Medium/ Medium', inplace = True)
    data['Skill Moves'].fillna(data['Skill Moves'].median(), inplace = True)
    data['Weak Foot'].fillna(3, inplace = True)
    data['Preferred Foot'].fillna('Right', inplace = True)
    data['International Reputation'].fillna(1, inplace = True)
    data['Wage'].fillna('€200K', inplace = True)

data_clean()
data.fillna(0, inplace = True)
