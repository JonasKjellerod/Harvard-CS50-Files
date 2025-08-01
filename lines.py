import sys

if len(sys.argv) < 1:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif sys.argv[1][-3:] != '.py':
    sys.exit('Not a Python file')
while True:
    try:
        with open(sys.argv[1]) as file:
            reader = file.read().split('\n')
            break
    except FileNotFoundError:
        sys.exit('File does not exist')
n = 0
for line in reader:
    if line.strip() != '' and line.strip().startswith('#') == False:
        n += 1
print(n)
