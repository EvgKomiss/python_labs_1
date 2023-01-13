import csv
from datetime import datetime


def second_task():
    years = []
    dates = {}
    with open("../Lab1/dataset.csv", 'r', newline='') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        for row in reader:
            date = str(row).split(",")[0][2:].replace("-", '')
            year = date[:4]
            if year not in years:
                years.append(str(row).split(",")[0][2:].split("-")[0])
                dates[year] = []
            dates[year].append(date)
        print(years[1:])


if __name__ == '__main__':
    second_task()