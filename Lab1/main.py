import json
import requests
import csv
from datetime import datetime

date = str(datetime.today().strftime('%Y/%m/%d'))
url = "http://www.cbr-xml-daily.ru/archive/" + date + "/daily_json.js"

if __name__ == '__main__':
    print(url)