# Class reader and writer are used
import csv

# When opening a new file, the newline should be '打开'
with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    # write rows
    data = [('1001', 'Sun', '21'), ('1002', 'Ming', 22)]
    writer.writerows(data)

