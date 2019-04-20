import pandas as pd
import numpy as np

def drop_duplicates(file):
    df = pd.read_csv(file, dtype={'lng': np.float32, 'lat': np.float32})
    df.drop_duplicates(inplace=True)
    df.to_csv('ok.csv', index=False)
if __name__ == '__main__':
    drop_duplicates("./AA00001-all.csv")
