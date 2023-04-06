import pandas as pd

languages = ["de", "en", "es", "fr", "ja", "zh"]

def loadData(filename):
    df = pd.read_csv(filename)
    return df


def storeData(filename,df):
    df.to_csv(filename, index=False)


def dropColumns(df,cols):
    df = df.drop(columns=cols)
    return df