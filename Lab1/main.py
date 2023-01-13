import json
import requests
import csv
from datetime import datetime


def data_collection(url: str, row_count: int = 15):
    """
    Takes URL and parses its content into dataset.csv file

    :param url: url of a page, containing json
    :param row_count: count of rows that will be scraped
    """
    with open("dataset.csv", 'w', newline='') as file:
        fieldnames = ['Date', 'Value']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(row_count):
            json_parse = json.loads(requests.get(url).text)
            url = "https:" + json_parse["PreviousURL"]
            date = str(json_parse["Date"])[0:-15]
            value = str(json_parse["Valute"]["USD"]["Value"])

            writer.writerow(
                {
                    "Date": date,
                    "Value": value
                }
            )


if __name__ == '__main__':
    date = str(datetime.today().strftime('%Y/%m/%d'))
    cur_url = "https://www.cbr-xml-daily.ru/archive/" + date + "/daily_json.js"
    data_collection(url=cur_url)
