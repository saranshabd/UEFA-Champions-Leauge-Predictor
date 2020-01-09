"""UEFA Champions Coefficient
Data Pre-processor, extracts data from the HTML into CSVs, clean that dataset

@author Shabd Saran
"""

import pandas as pd
from pandas import DataFrame


# import the tables from HTML file
with open('../data/html/uefa-coefficient.html') as file:
    df: DataFrame = pd.read_html(file)[19]

# clean the dataset
df = df.drop([('Ranking', '2020'), ('Ranking', '2019'), 
              ('Coefficient', 'Total'), ('Ranking', 'Mvmt'), 
              ('Coefficient', '2019–20')], axis=1)

# rename header to appropriate values
df.columns = ['Club', 'Country', 'C_2015-16', 'C_2016-17', 'C_2017-18', 
              'C_2018-19', 'C_Country']

# remove not interested teams
df = df[df['Club'].isin(['Real Madrid', 'Barcelona', 'Bayern Munich', 
        'Atlético Madrid', 'Juventus', 'Manchester City', 
        'Paris Saint-Germain', 'Liverpool','Tottenham Hotspur', 'Chelsea', 
        'Borussia Dortmund'])]

# set team name as the index
df.set_index('Club', inplace=True)

# store the computed result in a CSV file
df.to_csv('../data/data/uefa-coefficient.csv')
