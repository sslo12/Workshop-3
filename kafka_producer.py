import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import time
from kafka_conf.Kafka import kafka_producer


def ren_col_1516(df):
    column_mappings = {
        'Happiness Score': 'happiness_score',
        'Happiness Rank': 'happiness_rank',
        'Economy (GDP per Capita)': 'gdp_per_capita',
        'Family': 'social_support',
        'Health (Life Expectancy)': 'healthy_life_expectancy',
        'Trust (Government Corruption)': 'trust_government_corruption'}
    df.rename(columns=column_mappings, inplace=True)
    df.columns = [col.lower() for col in df.columns]
    return df[['country', 'happiness_rank', 'happiness_score', 'gdp_per_capita', 'social_support', 'freedom', 'healthy_life_expectancy', 'generosity', 'trust_government_corruption']]

def ren_col_17(df):
    column_mappings = {
        'Happiness.Score': 'happiness_score',
        'Happiness.Rank': 'happiness_rank',
        'Economy..GDP.per.Capita.': 'gdp_per_capita',
        'Family': 'social_support',
        'Health..Life.Expectancy.': 'healthy_life_expectancy',
        'Trust..Government.Corruption.': 'trust_government_corruption'}
    df.rename(columns=column_mappings, inplace=True)
    df.columns = [col.lower() for col in df.columns]
    return df[['country', 'happiness_rank', 'happiness_score', 'gdp_per_capita', 'social_support', 'freedom', 'healthy_life_expectancy', 'generosity', 'trust_government_corruption']]

def ren_col_1819(df):
    column_mappings = {
        'Country or region': 'country',
        'Overall rank': 'happiness_rank',
        'Score': 'happiness_score',
        'GDP per capita': 'gdp_per_capita',
        'Social support': 'social_support',
        'Freedom to make life choices': 'freedom',
        'Healthy life expectancy': 'healthy_life_expectancy',
        'Perceptions of corruption': 'trust_government_corruption',
        'Generosity': 'generosity'}
    df.rename(columns=column_mappings, inplace=True)
    df.columns = [col.lower() for col in df.columns]
    return df[['country', 'happiness_rank', 'happiness_score', 'gdp_per_capita', 'social_support', 'freedom', 'healthy_life_expectancy', 'generosity', 'trust_government_corruption']]

def concat_df(df_list):
    columns_set = {tuple(df.columns) for df in df_list}
    if len(columns_set) != 1:
        raise ValueError("All DataFrames must have the same columns to concatenate. Please check the column names.")
    concate_df = pd.concat(df_list, ignore_index=True)
    return concate_df

def etl():
    df_15 = pd.read_csv('./Datasets/2015.csv')
    new_2015 = ren_col_1516(df_15)
    df_16 = pd.read_csv('./Datasets/2016.csv')
    new_2016 = ren_col_1516(df_16)
    df_17 = pd.read_csv('./Datasets/2017.csv')
    new_2017 = ren_col_17(df_17)
    df_18 = pd.read_csv('./Datasets/2018.csv')
    new_2018 = ren_col_1819(df_18)
    df_19 = pd.read_csv('./Datasets/2019.csv')
    new_2019 = ren_col_1819(df_19)

    dfs_news = [new_2015, new_2016, new_2017, new_2018, new_2019]
    new_happy_world = concat_df(dfs_news)
    new_happy_world.dropna(inplace=True)
    colum_drop = ['happiness_rank','generosity','trust_government_corruption']
    new_happy_world.drop(columns=colum_drop, inplace=True)
    return new_happy_world

def model_training(df):
    new_happy = df.select_dtypes(include=[np.number])
    X = new_happy.drop('happiness_score',axis= 1)
    y = new_happy['happiness_score'] 
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3, random_state=20)
    return df.iloc[y_test.index]


if __name__ == "__main__":
    new_happy_df = etl()
    new_happy_df = model_training(new_happy_df)
    for index, row in new_happy_df.iterrows():
        kafka_producer(row)