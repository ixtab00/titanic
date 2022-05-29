import csv
import numpy
from typing import Dict, List
import os

IGNORE = ['PassengerId', 'Survived', 'Name', 'Fare']
ENCODE_IGNORE = ['Age']
IN_COUNT = ['Parch', 'Pclass', 'SibSp', 'Age', 'Sex']

def read(file: str) -> List:
    with open(file) as file:
        reader = csv.DictReader(file)
        data_as_list = []
        for row in reader:
            data_as_list.append(row)
        return data_as_list


def get_data_types(data: List[Dict]) -> Dict:
    val_vals = {}
    for key in data[0].keys():
        if key not in IGNORE:
            val_vals[key] = []
            for i in range(len(data)):
                if data[i][key] not in val_vals[key]:
                    val_vals[key].append(data[i][key])
        for key in val_vals.keys():
            val_vals[key].sort()
    return val_vals


def getfl_match(data: Dict, as_float: Dict, as_str: Dict):
    match = {}
    for key in as_float:
        match[key] = {}
        source = data[key]
        source_asfl = []
        for i in range(len(source)):
            try:
                source_asfl.append(float(source[i]))
            except: 
                source_asfl.append(0)
        
        max_num = max(source_asfl)
        for rec in source:
            if rec != '':
                match[key][rec] = float(rec)/max_num
            else:
                match[key][rec] = 0
        
    for key in as_str:
        match[key] = {}
        max_num = len(data[key]) -1
        for i, rec in enumerate(data[key]):
            match[key][rec] = i/max_num
    
    match['Ticket'] = {}
    source = data['Ticket']
    source_copy = []
    for tck in source:
        tck_p = tck.split(' ')
        source_copy.append(tck_p[-1])
    for i in range(len(source)):
        try:
            source_asfl.append(float(source_copy[i]))
        except: 
            source_asfl.append(0)
        
    max_num = max(source_asfl)
    for rec in source:
        try:
            match[key][rec] = float(rec)/max_num
        except:
            match[key][rec] = 0
    return match


def encode_data(data: List, match: Dict):
    encoded = numpy.zeros((len(data), len(IN_COUNT)))
    for i in range(len(IN_COUNT)):
        for j in range(len(data)):
            encoded[j][i] = match[IN_COUNT[i]][data[j][IN_COUNT[i]]]
    return encoded

def prep_ans(data: List):
    encoded = numpy.zeros((len(data), 1))
    for i in range(len(data)):
        encoded[i][0] = float(data[i]['Survived'])
    return encoded