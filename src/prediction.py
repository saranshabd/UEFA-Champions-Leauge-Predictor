import pandas as pd
import numpy as np
from numpy import array
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier


'''Import the dataset'''

df: DataFrame = pd.read_csv('../data/data/final-dataset.csv', encoding='utf-8')
df['Pos'] = 4 - df['Pos']


'''Differentiate Features and Label'''

X: array = df.iloc[:, 1:-1].values
y: array = df.iloc[:, -1].values

    
'''Create instance of Random Forest Classifier and train the model'''

classifier = RandomForestClassifier(n_estimators=10, criterion='entropy')
classifier.fit(X, y)


def get_ucl_stage(standing: int) -> str:
    """Convert UCL Standing Integer into its corresponding String value"""
    
    if 1 == standing:
        return 'Group Stage'
    elif 2 == standing:
        return 'Round 16'
    elif 3 == standing:
        return 'Quarter Finals'
    elif 4 == standing:
        return 'Semi Finals'
    else:
        return 'Finals'


def prediction(pos: int, pts: int, gd: int, qualify: int) -> str:
    """Predicts the level at which the team will go on in 2019-20 season"""
    
    X_test: array = array([[pos, pts, gd, qualify]])
    
    return get_ucl_stage(int(classifier.predict(X_test)[0]))


'''Make Predictions'''

predictions: dict = {}

predictions['Real Madrid'] = prediction(pos=2, pts=11, gd=6, qualify=1)
predictions['Barcelona'] = prediction(pos=1, pts=14, gd=5, qualify=1)
predictions['Bayern Munich'] = prediction(pos=1, pts=18, gd=19, qualify=1)
predictions['Tottenham Hotspur'] = prediction(pos=2, pts=10, gd=4, qualify=1)
predictions['Manchester City'] = prediction(pos=1, pts=14, gd=12, qualify=1)
predictions['Juventus'] = prediction(pos=1, pts=16, gd=8, qualify=1)
predictions['Atlético Madrid'] = prediction(pos=2, pts=10, gd=3, qualify=1)
predictions['Liverpool'] = prediction(pos=1, pts=13, gd=5, qualify=1)
predictions['Borussia Dortmund'] = prediction(pos=2, pts=10, gd=7, qualify=1)
predictions['Chelsea'] = prediction(pos=2, pts=11, gd=2, qualify=1)
predictions['Paris Saint-Germain'] = prediction(pos=1, pts=16, gd=15, qualify=1)


'''Store predictions in a CSV file'''

prediction_df: DataFrame = DataFrame(columns=['Club', 'Standing'])
for club, standing in predictions.items():
    prediction_df = prediction_df.append([{'Club': club, 'Standing': standing}])
prediction_df.set_index('Club', inplace=True)
prediction_df.to_csv('../data/data/predictions.csv', encoding='utf-8')
