import csv
import json

CSV_FILE_PATH = 'resources/cars.csv'
JSON_FILE_PATH = 'resources/cars.json'

with open(CSV_FILE_PATH) as cars:
    file_reader = csv.DictReader(cars)
    data = []
    for row in file_reader:
        data.append(row)
print(data)

with open(JSON_FILE_PATH, 'w') as json_cars:
    json.dump(data, json_cars, indent=2)
