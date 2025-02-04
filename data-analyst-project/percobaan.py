import pandas as pd

def load_data(filename):
    return pd.read_csv("./data/raw/ecommerce_dataset.csv")

if __name__ == '__percobaan__':
    percobaan()