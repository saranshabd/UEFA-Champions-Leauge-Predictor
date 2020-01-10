import pandas as pd
import numpy as np
from pandas import DataFrame


def adjust_df(df: DataFrame, season: str) -> DataFrame:
    """Adjust Club row values and all the other column names"""
    
    df.columns = ['Club', 'Pos', 'Pts', 'GD', 'Qualify']
    df['Club'] = df['Club'] + f'_{season}'
    
    return df


'''Create new DataFrame for each season'''

df1: DataFrame = pd.read_csv('../data/data/group-stage-2014-15.csv', encoding='utf-8')
df1 = adjust_df(df1, '2014-15')

df2: DataFrame = pd.read_csv('../data/data/group-stage-2015-16.csv', encoding='utf-8')
df2 = adjust_df(df2, '2015-16')

df3: DataFrame = pd.read_csv('../data/data/group-stage-2016-17.csv', encoding='utf-8')
df3 = adjust_df(df3, '2016-17')

df4: DataFrame = pd.read_csv('../data/data/group-stage-2017-18.csv', encoding='utf-8')
df4 = adjust_df(df4, '2017-18')

df5: DataFrame = pd.read_csv('../data/data/group-stage-2018-19.csv', encoding='utf-8')
df5 = adjust_df(df5, '2018-19')


'''Create new DataFrame to the results of all the seasons'''

df: DataFrame = pd.concat([df1, df2, df3, df4, df5])
df = df.set_index('Club')


'''Create new Dataframe to UCL Standings'''

ucl_standings: DataFrame = pd.read_csv('../data/data/uefa-standings.csv', encoding='utf-8')
df_standings = DataFrame(columns=['Club', 'Standing'])
for i in range(len(ucl_standings)):
    df_standings = df_standings.append([
        {
            'Club': ucl_standings.iloc[i]['Club'] + '_2014-15',
            'Standing': ucl_standings.iloc[i]['Standing_2014-15']
        },
        {
            'Club': ucl_standings.iloc[i]['Club'] + '_2015-16',
            'Standing': ucl_standings.iloc[i]['Standing_2015-16']
        },
        {
            'Club': ucl_standings.iloc[i]['Club'] + '_2016-17',
            'Standing': ucl_standings.iloc[i]['Standing_2016-17']
        },
        {
            'Club': ucl_standings.iloc[i]['Club'] + '_2017-18',
            'Standing': ucl_standings.iloc[i]['Standing_2017-18']
        },
        {
            'Club': ucl_standings.iloc[i]['Club'] + '_2018-19',
            'Standing': ucl_standings.iloc[i]['Standing_2018-19']
        }
    ])
df_standings.set_index('Club', inplace=True)


'''Sort both the Dataframes by Index (Club)'''

df.sort_index(inplace=True)
df_standings.sort_index(inplace=True)


'''Add UCL Standing of all the teams to the Dataset'''

df['Standing'] = df_standings[df.index == df_standings.index]['Standing']
df.sort_index(inplace=True)


'''Remove data of all the teams which did not take part in the UCL'''

df.replace(-9999, np.NaN, inplace=True)
df.dropna(inplace=True)


'''Store computed results into a CSV file'''

df.to_csv('../data/data/final-dataset.csv', encoding='utf-8')
