import csv
import json

CSV_FILE_PATH = 'resources/cars.csv'
JSON_FILE_PATH = 'resources/cars.json'
fieldnames = ('Year', 'Make', 'Model')

with open(CSV_FILE_PATH) as cars:
    file_reader = csv.DictReader(cars, fieldnames)
    next(file_reader)
    data = []
    for row in file_reader:
        data.append(row)
print(data)

with open(JSON_FILE_PATH, 'w') as json_cars:
    json.dump(data, json_cars, indent=2)
