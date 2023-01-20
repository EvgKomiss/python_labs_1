import pandas
import matplotlib


def read_data(path: str = '../Lab1/dataset.csv') -> pandas.DataFrame:
    return pandas.read_csv(path)


def rename_columns(df: pandas.DataFrame) -> pandas.DataFrame:
    return df.rename(columns={'Date': 'date', 'Value': 'value'})


def drop_invalid_rows(df: pandas.DataFrame) -> pandas.DataFrame:
    return df.replace(to_replace='None', value=pandas.NaT).replace(to_replace="NaT", value=pandas.NaT).dropna()


if __name__ == '__main__':
    print(drop_invalid_rows(rename_columns(read_data())))
