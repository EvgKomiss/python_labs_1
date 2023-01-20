import pandas
import matplotlib


def read_data(path: str = '../Lab1/dataset.csv'):
    return pandas.read_csv(path)


if __name__ == '__main__':
    print(read_data())
