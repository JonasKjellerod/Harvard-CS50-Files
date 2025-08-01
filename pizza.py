import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif sys.argv[1][-4:] != '.csv':
    print
    sys.exit('Not a CSV file')
rows = []
with open(sys.argv[1], 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        rows.append(row)

headers = rows[0]
table = rows[1:]

print(tabulate(table,headers,tablefmt="grid"))
