import csv

with open('test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        print(', '.join(row))

# sniffer: to inference the format of a csv file
with open('test.csv', newline='') as csvfile:
    # Here the dialect is used for the parser
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    for row in reader:
        print(row)
