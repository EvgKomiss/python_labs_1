import pandas
import datetime
from utils import file_writer
from datetime import datetime, timedelta


def second_task(df: pandas.DataFrame):
    date = df["Date"].tolist()
    value = df["Value"].tolist()

    date_copy = {}
    for i in range(len(date)):
        row_date = datetime.strptime(date[i], '%Y-%m-%d').date()
        if row_date.year not in date_copy.keys():
            date_copy[row_date.year] = []
        date_copy[row_date.year].append((row_date, value[i]))
    for i in date_copy:
        file_writer(date_copy[i])