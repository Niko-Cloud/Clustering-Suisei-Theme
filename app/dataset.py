import pandas as pd

def read_csv():
    dataset = pd.read_csv('./BankNote_Authentication.csv')
    return dataset