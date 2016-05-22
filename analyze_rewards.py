import pandas as pd

# formatting the already created csv

def dataframe_rewards(csvname):

    df = pd.read_csv(csvname, header=0)
    df['date'] = pd.to_datetime(df['date'])
    df['reward'] = pd.to_numeric(df['reward'])
    df['cumulative'] = pd.to_numeric(df['cumulative'])
    
    df.sort_values('date', ascending=False, inplace=True)
    df.reset_index(inplace=True, drop=True)
    
    df.to_csv(csvname, index=False)