import csv


def file_writer(date: list):
    min_date = str(min(date, key=lambda t: t[0])[0]).replace('-', '')
    max_date = str(max(date, key=lambda t: t[0])[0]).replace('-', '')
    with open(f"{min_date}_"f"{max_date}", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(date)