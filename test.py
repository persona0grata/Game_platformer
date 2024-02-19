import csv

csv_file_path = 'Map.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

for row in data_list:
    print(row)
