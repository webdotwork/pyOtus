import csv
from csv import DictReader


def csv_reader(csv_file_path: str) -> []:

    out = list()

    with open(csv_file_path, newline='') as f:
        reader = DictReader(f)
        # Итерируемся по данным делая из них словари
        for row in reader:
            out.append(row)

    return out
