import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    
    df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed",
    dayfirst=True
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        format="mixed",
        dayfirst=True
    )
    
    df["Postal Code"] = df["Postal Code"].fillna(0)
    
    return df