import csv
from io import StringIO

def readString(string_data):
    result = []
    string_data = string_data.split("\n")
    for row in string_data:
        if (row[0].isdigit() == True):
            result.append(eval(row))
    return result


def task(csv_string):
    data = readString(csv_string)

    row1 = {}
    row2 = {}

    for [r1, r2] in data:
        row1[r1] = r1
        row2[r2] = True

    row3 = {}
    row4 = {}
    row5 = {}

    for [l, r] in data:
        for [i, j] in data:
            if r == i:
                row3[l] = True
                row4[j] = True
            if (l == i) & (r != j):
                row5[r] = True

    return [list(row1.keys()), list(row2.keys()), list(row3.keys()), list(row4.keys()), list(row5.keys())] 