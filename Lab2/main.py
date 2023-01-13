import pandas
import csv
from datetime import datetime


def first_task(df: pandas.DataFrame):
    date = df["Date"].tolist()
    value = df["Value"].tolist()

    with open("X.csv", "w", newline='') as f:
        for i in date:
            writer = csv.writer(f)
            writer.writerow([i])

    with open("Y.csv", "w", newline='') as f:
        for i in value:
            writer = csv.writer(f)
            writer.writerow([i])


def second_task(df: pandas.DataFrame):
    pass


def third_task(df: pandas.DataFrame):
    pass


if __name__ == '__main__':
    dataframe = pandas.read_csv("../Lab1/dataset.csv")
    first_task(dataframe)
    second_task(dataframe)
    third_task(dataframe)
