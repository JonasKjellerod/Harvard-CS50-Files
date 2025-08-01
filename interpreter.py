[x,y,z] = input('Calculate ').split(' ')

value = 0

if y == '+':
    value = float(x) + float(z)
elif y == '-':
    value = float(x) - float(z)
elif y == '*':
    value = float(x) * float(z)
elif y == '/':
    value = float(x) / float(z)

print(value)
