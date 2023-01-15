import pandas
import csv


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