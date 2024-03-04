import pandas as pd

def WriteToXelx_def(dict):
    df = pd.DataFrame(dict)
    df.to_excel('Book_from_chitay_gorod.xlsx')