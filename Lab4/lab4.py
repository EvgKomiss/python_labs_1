import pandas
import matplotlib


def read_data(path: str = '../Lab1/dataset.csv') -> pandas.DataFrame:
    return pandas.read_csv(path)


def rename_columns(df: pandas.DataFrame) -> pandas.DataFrame:
    return df.rename(columns={'Date': 'date', 'Value': 'value'})


if __name__ == '__main__':
    print(rename_columns(read_data()))
