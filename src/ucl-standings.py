"""UEFA Champions Standings from season 2014-15 to 2018-19
Manuak data registration

@author Shabd Saran
"""

import pandas as pd
import numpy as np
from pandas import DataFrame


# create new DataFrame
df: DataFrame = pd.DataFrame(columns=['Club', 'Standing_2014-15', 
                                      'Standing_2015-16', 'Standing_2016-17', 
                                      'Standing_2017-18','Standing_2018-19'],
                        dtype=np.int64)


def create_new_entry(df: DataFrame, club: str, standing14: int,
                     standing15: int, standing16: int, standing17: int,
                     standing18: int) -> DataFrame:
    """create new entry in the DataFrame"""
    
    return df.append([{
                'Club': club,
                'Standing_2014-15': standing14,
                'Standing_2015-16': standing15,
                'Standing_2016-17': standing16,
                'Standing_2017-18': standing17,
                'Standing_2018-19': standing18,
            }])


# store new entries into the DataFrame
df = create_new_entry(df, 'Real Madrid', 4, 5, 5, 5, 2)
df = create_new_entry(df, 'Barcelona', 5, 3, 3, 3, 4)
df = create_new_entry(df, 'Bayern Munich', 4, 4, 3, 4, 2)
df = create_new_entry(df, 'Atlético Madrid', 3, 5, 4, 1, 2)
df = create_new_entry(df, 'Juventus', 5, 2, 5, 3, 3)
df = create_new_entry(df, 'Manchester City', 2, 4, 2, 3, 3)
df = create_new_entry(df, 'Paris Saint-Germain', 3, 3, 2, 2, 2)
df = create_new_entry(df, 'Liverpool', 1, -9999, -9999, 5, 5)
df = create_new_entry(df, 'Tottenham Hotspur', -9999, -9999, 1, 2, 5)
df = create_new_entry(df, 'Chelsea', 2, 2, -9999, 2, -9999)
df = create_new_entry(df, 'Borussia Dortmund', 2, -9999, 3, 1, 2)
    
df.set_index('Club', inplace=True)

# store computed results in a CSV file
df.to_csv('../data/data/uefa-standings.csv')
