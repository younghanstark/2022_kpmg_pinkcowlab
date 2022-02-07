import pandas as pd

def read_data(filename):
    return pd.read_excel('./core/test_data/'+filename+'.xlsx')
