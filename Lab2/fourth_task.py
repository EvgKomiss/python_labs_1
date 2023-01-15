from datetime import datetime
from utils import get_data
import os


def first_type(date: datetime.date = None) -> float or None:
    dates = get_data("X.csv")["Date"].tolist()
    try:
        index = dates.index(str(date))
    except ValueError:
        return None
    return get_data("Y.csv")["Value"].tolist()[index]


def second_type(date: datetime.date = None) -> float or None:
    path = None
    for file in os.listdir():
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
    if path is None:
        return None
    data = get_data(path)
    result = data.loc[data["Date"] == str(date)]["Value"].tolist()[0]
    return result


if __name__ == '__main__':
    second_type()
