import pandas
import matplotlib


def read_data(path: str = '../Lab1/dataset.csv') -> pandas.DataFrame:
    df = pandas.read_csv(path)
    df = drop_invalid_rows(df)
    df['Date'] = pandas.to_datetime(df['Date'], format='%Y-%m-%d')
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


if __name__ == '__main__':
    print(create_value_deviation_columns(rename_columns(read_data())))
