import pandas
from datetime import datetime, timedelta
from utils import file_writer, get_data


def third_task(df: pandas.DataFrame) -> None:
    """
    Splices a given dataframe into N files, categorized by weeks.

    :param df: Dataframe to be spliced
    """
    date = df["Date"].tolist()
    value = df["Value"].tolist()

    tmp_list = []
    for i in range(len(date)):
        row_date = datetime.strptime(date[i], '%Y-%m-%d').date()
        day_of_the_week = row_date.isocalendar().weekday
        if len(tmp_list) >= 2:
            day_of_the_week_buffer = tmp_list[-1][0].isocalendar().weekday
            weekday_checker = day_of_the_week_buffer - day_of_the_week
            date_checker = tmp_list[-1][0] - row_date
            if weekday_checker <= 0 or date_checker >= timedelta(days=7):
                file_writer(tmp_list)
                tmp_list = [(row_date, value[i])]
            else:
                tmp_list.append((row_date, value[i]))
        else:
            tmp_list.append((row_date, value[i]))
        if day_of_the_week == 0:
            file_writer(tmp_list)
            tmp_list = []


if __name__ == '__main__':
    third_task(get_data())
