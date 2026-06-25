import csv
import datetime
from pathlib import Path


class LogItem:
    date_now = datetime.datetime.now()


def get_month():
    return LogItem.date_now.strftime("%B")


def get_year():
    return LogItem.date_now.strftime("%y")


def get_date():
    return LogItem.date_now.strftime("%d-%m-%Y")


def get_time():
    return LogItem.date_now.strftime("%H:%M:%S")


class csvTools:
    folder_name = Path(f"{get_month()}{get_year()}")
    file_name = f"{get_month()}{get_year()}.csv"

    file_path = folder_name / file_name

    field_names = ["Date", "Time In", "Time Out"]


def mkFolder():
    csvTools.folder_name.mkdir(parents=True, exist_ok=True)


def logIn():
    mkFolder()

    file_exists = csvTools.file_path.is_file()
    
    with open(
        csvTools.file_path, mode="a", newline="", encoding="utf-8"
    ) as csv_file:
        row_writer = csv.DictWriter(
            csv_file, fieldnames=csvTools.field_names, quoting=csv.QUOTE_MINIMAL
        )

        if not file_exists:
            row_writer.writeheader()

        row_writer.writerow({"Date": get_date(), "Time In": get_time()})


def logOut():
    mkFolder()

    file_exists = csvTools.file_path.is_file()
    
    with open(
        csvTools.file_path, mode="a", newline="", encoding="utf-8"
    ) as csv_file:
        row_writer = csv.DictWriter(
            csv_file, fieldnames=csvTools.field_names, quoting=csv.QUOTE_MINIMAL
        )

        if not file_exists:
            row_writer.writeheader()

        row_writer.writerow({"Date": get_date(), "Time Out": get_time()})

if __name__ == "__main__":
    logIn()