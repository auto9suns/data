import pandas as pd
import argparse

def schema_from_df(df):
    '''
    :param df: dataframe
    :return:
    '''
    schema = df.dtypes.apply(lambda x: x.name).to_dict()
    print(schema)
    return schema

def import_csv(csvpath):
    return pd.read_csv(csvpath)

def schema_to_sql(schema):
    '''
    :param schema: schema dict
    :return:
    '''
    pass





if __name__ == "__main__":
    schema_from_df(import_csv("orders.csv"))