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
    date = df["Date"].tolist()
    value = df["Value"].tolist()

    date_copy = {}
    i: str
    for i in range(len(date)):
        row_date = datetime.strptime(date[i], '%Y-%m-%d').date()
        if row_date.year not in date_copy.keys():
            date_copy[row_date.year] = []
        date_copy[row_date.year].append((row_date, value[i]))
    for i in date_copy:
        min_date = str(min(date_copy[i], key=lambda t:t[0])[0]).replace('-', '')
        max_date = str(max(date_copy[i], key=lambda t:t[0])[0]).replace('-', '')
        with open(f"{min_date}_"f"{max_date}", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(date_copy[i])


def third_task(df: pandas.DataFrame):
    pass


if __name__ == '__main__':
    dataframe = pandas.read_csv("../Lab1/dataset.csv")
    first_task(dataframe)
    second_task(dataframe)
    third_task(dataframe)
