import pandas as pd
import os

path = os.path.dirname(os.path.realpath(__file__))

def read_data(filename):
    return pd.read_excel(path+'/test_data/'+filename+'.xlsx')
