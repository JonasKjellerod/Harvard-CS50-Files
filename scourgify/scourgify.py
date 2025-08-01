import csv
import sys


if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

students = []

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        last, first = row['name'].split(', ')
        house = row['house']
        students.append({'first': first, 'last': last, 'house': house})

with open(sys.argv[2], 'w') as file:
    writer = csv.DictWriter(file, fieldnames = ['first','last','house'])
    writer.writeheader()
    for student in students:
        writer.writerow(student)



