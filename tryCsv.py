import csv


with open('geoinfo.csv', encoding="ISO-8859-1") as file:
    vari = csv.DictReader(file)
    reader = list(vari)
print(reader[0:3])
print(len(reader))
print(reader[0].keys())