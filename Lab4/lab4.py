from datetime import datetime
import pandas
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
matplotlib.use('TkAgg')


def read_data(path: str = '../Lab1/dataset.csv') -> pandas.DataFrame:
    df = pandas.read_csv(path)
    df = drop_invalid_rows(df)
    df['Date'] = pandas.to_datetime(df['Date'], format='%Y-%m-%d',)
    df['Value'] = pandas.to_numeric(df['Value'])
    return df


def rename_columns(df: pandas.DataFrame) -> pandas.DataFrame:
    return df.rename(columns={'Date': 'date', 'Value': 'value'})


def drop_invalid_rows(df: pandas.DataFrame) -> pandas.DataFrame:
    return df.replace(to_replace='None', value=pandas.NaT).replace(to_replace="NaT", value=pandas.NaT).dropna()


def create_value_deviation_columns(df: pandas.DataFrame) -> pandas.DataFrame:
    df['median_dev'] = df['value'] - df['value'].median()
    df['mean_dev'] = df['value'] - df['value'].mean()
    return df


def write_statistics(df: pandas.DataFrame) -> None:
    print(df.agg({'value': ['min', 'max', 'median', 'mean'],
                  'median_dev': ['min', 'max', 'median', 'mean'],
                  'mean_dev': ['min', 'max', 'median', 'mean']}))


def filter_by_deviation(df: pandas.DataFrame, deviation: float or int) -> pandas.DataFrame:
    return df[df['mean_dev'] >= deviation]


def filter_by_date(df: pandas.DataFrame, start_date: datetime.date, end_date: datetime.date):
    return df.loc[df['date'].between(start_date, end_date)]


def group_by_month_mean(df: pandas.DataFrame) -> pandas.DataFrame:
    return df.groupby(df['date'].dt.month)['value'].mean()


def group_by_month_median(df: pandas.DataFrame) -> pandas.DataFrame:
    return df.groupby(df['date'].dt.month)['value'].median()


def draw_global_chart(df: pandas.DataFrame, title: str = '') -> None:
    plt.figure('Global value chart')
    plt.plot(df['date'], df['value'], color="green")
    plt.xlabel('Date')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()
    plt.ylabel('Value')
    plt.title(title, loc='left')
    plt.show()


def draw_monthly_chart(df: pandas.DataFrame, month: int) -> None:
    df = df[df['date'].dt.month == month]
    dfs = [df[df['date'].dt.year == y] for y in df['date'].dt.year.unique()]
    for df in dfs:
        mean = group_by_month_mean(df).reset_index()['value'].tolist()[0]
        median = group_by_month_median(df).reset_index()['value'].tolist()[0]
        title = "Mean: " + str(mean) + "    Median: " + str(median)
        draw_global_chart(df, title)


if __name__ == '__main__':
    new_df = create_value_deviation_columns(rename_columns(read_data()))
    write_statistics(new_df)
    print(filter_by_deviation(new_df, 2.37))
    print(filter_by_date(new_df, datetime(2022, 10, 12), datetime(2022, 10, 14)))
    print(group_by_month_mean(new_df))
    draw_global_chart(new_df)
    draw_monthly_chart(new_df, 11)
