import csv
import os

os.chdir(os.path.dirname(__file__))

FILE_NAME = os.getcwd() + "/csv_iris.csv"

with open(FILE_NAME, encoding='UTF-8') as file:
    header_names = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    content = csv.DictReader(file, fieldnames=header_names, delimiter=",", quotechar='"')
    for row in content:
        if content.line_num == 1:
            continue
        print(row['Sepal length'], row['Sepal width'], row['Petal length'], row['Petal width'], row['Species'])

