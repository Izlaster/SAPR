import numpy as np

def readCSV(csv_file):
    with open(csv_file) as file:
        pre_result = []
        result = []
        my_row = []
        csv_string = file.read()
        csv_string = csv_string.split("\n")
        for row in csv_string:
            pre_result.append(eval(row))
        for i in range(0, len(pre_result[0])):
            for j in range(0, len(pre_result[0])):
                my_row.append(pre_result[j][i])
            result.append(my_row)
            my_row = []
    return result

def makeMyMatrix(matrix):
    arr_matrix = []
    new_row = []
    for k in range(0, len(matrix)):
        for i in range(0, len(matrix[k])):
            for j in range(0, len(matrix[k])):
                if (matrix[k][i] < matrix[k][j]):
                    new_row.append(1)
                elif (matrix[k][i] == matrix[k][j]):
                    new_row.append(0.5)
                elif (matrix[k][i] > matrix[k][j]):
                    new_row.append(0)
        arr_matrix.append(new_row)
        new_row = []
    return arr_matrix

res = readCSV("./task6_data.csv")
print(makeMyMatrix(res))