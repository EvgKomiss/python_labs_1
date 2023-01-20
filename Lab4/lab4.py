from datetime import datetime
import pandas
import matplotlib


def read_data(path: str = '../Lab1/dataset.csv') -> pandas.DataFrame:
    df = pandas.read_csv(path)
    df = drop_invalid_rows(df)
    df['Date'] = pandas.to_datetime(df['Date'], format='%Y-%m-%d',)
    df['Value'] = pandas.to_numeric(df['Value'])
    return df


def rename_columns(df: pandas.DataFrame) -> pandas.DataFrame:
    return df.rename(columns={'Date': 'date', 'Value': 'value'})


def drop_invalid_rows(df: pandas.DataFrame) -> pandas.DataFrame:
    return df.replace(to_replace='None', value=pandas.NaT).replace(to_replace="NaT", value=pandas.NaT).dropna()


def create_value_deviation_columns(df: pandas.DataFrame) -> pandas.DataFrame:
    df['median_dev'] = df['value'] - df['value'].median()
    df['mean_dev'] = df['value'] - df['value'].mean()
    return df


def write_statistics(df: pandas.DataFrame) -> None:
    print(df.agg({'value': ['min', 'max', 'median', 'mean'],
                  'median_dev': ['min', 'max', 'median', 'mean'],
                  'mean_dev': ['min', 'max', 'median', 'mean']}))


def filter_by_deviation(df: pandas.DataFrame, deviation: float or int) -> pandas.DataFrame:
    return df[df['mean_dev'] >= deviation]


def filter_by_date(df: pandas.DataFrame, start_date: datetime.date, end_date: datetime.date):
    return df.loc[df['date'].between(start_date, end_date)]


if __name__ == '__main__':
    new_df = create_value_deviation_columns(rename_columns(read_data()))
    write_statistics(new_df)
    print(filter_by_deviation(new_df, 2.37))
    print(filter_by_date(new_df, datetime(2022, 10, 12), datetime(2022, 10, 14)))
