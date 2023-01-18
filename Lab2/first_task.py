import pandas
import csv
from Lab2.utils import get_data


def first_task(df: pandas.DataFrame, path: str) -> None:
    """
    Splices given dataframe into two files. One with dates, and one with values.

    :param df: Dataframe to be spliced
    :param path: Path to the new files
    """
    date = df["Date"].tolist()
    value = df["Value"].tolist()

    with open(path + "/X.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow({"Date"})
        for i in date:
            writer.writerow([i])

    with open(path + "/Y.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow({"Value"})
        for i in value:
            writer.writerow([i])


if __name__ == '__main__':
    first_task(get_data(), "./test")
