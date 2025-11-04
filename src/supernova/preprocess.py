import pandas as pd

def load_and_clean(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df = df.dropna().reset_index(drop=True)
    return df
