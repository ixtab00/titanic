import csv
from os import curdir, path
from typing import List

def read(file: str):
    with open(file) as file:
        reader = csv.DictReader(file)
        data_as_list = []
        for row in reader:
            data_as_list.append(row)
        return row