import csv

FILENAME = r'csv_writer.csv'

DATABASE = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Max', 'last_name': 'Peck'},
    {'first_name': 'Ivan'},
    {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
    {'first_name': 'Jose', 'born': 1961, 'first_step': 1969},
]

headers = set()
for dict in DATABASE:
    for key in dict.keys():
        headers.add(key)

# headers_lst = list(headers)

# print(headers_lst)

with open(FILENAME, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=headers,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in DATABASE:
        writer.writerow(row)