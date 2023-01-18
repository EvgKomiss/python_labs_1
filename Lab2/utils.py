import csv
import pandas


def file_writer(date: list, path: str) -> None:
    """
    Creates a .csv file from given data. Automatically correctly names it.

    :param date: Data to be written
    :param path: Path to the new files
    """
    min_date = str(min(date, key=lambda t: t[0])[0]).replace('-', '')
    max_date = str(max(date, key=lambda t: t[0])[0]).replace('-', '')
    with open(path + f"/{min_date}_{max_date}.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow({"Date", "Value"})
        writer.writerows(date)


def get_data(path: str = "../Lab1/dataset.csv") -> pandas.DataFrame:
    """
    Returns a dataframe, generated from given .csv file.

    :param path: Path to readable .csv file
    :return: Dataframe
    """
    return pandas.read_csv(path)
