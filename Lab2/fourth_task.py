from datetime import datetime
from Lab2.utils import get_data
import os


def default_type(date: datetime.date = None, path: str = None) -> float or None:
    """
    Searches for given date and returns value for it.

    :param date: Date to search
    :param path: Path to files
    :return: Value for given date
    """
    try:
        data = get_data(path + "/dataset.csv")
    except FileNotFoundError:
        return "Error occurred. Bad path"
    dates = data["Date"].tolist()
    try:
        index = dates.index(str(date))
    except ValueError:
        return None
    try:
        result = data["Value"].tolist()[index]
    except FileNotFoundError:
        return "Error occurred. Bad path"
    return result


def first_type(date: datetime.date = None, path: str = None) -> float or None:
    """
    Searches for given date and returns value for it.

    :param date: Date to search
    :param path: Path to files
    :return: Value for given date
    """
    try:
        dates = get_data(path + "/X.csv")["Date"].tolist()
        try:
            index = dates.index(str(date))
        except ValueError:
            return None
        result = get_data(path + "/Y.csv")["Value"].tolist()[index]
    except FileNotFoundError:
        return "Error occurred. Bad path"
    return result


def second_type(date: datetime.date = None, pather: str = None) -> float or None:
    """
    Searches for given date and returns value for it.

    :param date: Date to search
    :param pather: Path to files
    :return: Value for given date
    """
    path = None
    try:
        for file in os.listdir(pather):
            if file.endswith(".csv"):
                tmp = file
                potential_file = file.replace(".csv", "").split("_")
                date_value = -1
                try:
                    data_range = int(potential_file[1]) - int(potential_file[0])
                    date_value = int(potential_file[1]) - int(str(date).replace("-", ""))
                except IndexError:
                    data_range = -1
                if data_range >= date_value >= 0:
                    path = tmp
                    break
        if path is None:
            return None
        data = get_data(pather + "/" + path)
        result = data.loc[data["Date"] == str(date)]["Value"].tolist()[0]
    except FileNotFoundError:
        return "Error occurred. Bad path"
    return result


def my_next(counter: int, file_name: str = "20220610_20221231.csv") -> tuple:
    """
    Returns next available value in given file.

    :param counter: Current row in given file
    :param file_name: File to iterate
    :return: Current date and value
    """
    data = get_data(file_name)
    date = data["Date"].tolist()
    value = data["Value"].tolist()
    return date[-counter], value[-counter]


if __name__ == '__main__':
    print(second_type(datetime(2022, 12, 14).date(), ''))
