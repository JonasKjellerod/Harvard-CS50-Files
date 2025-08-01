camel = input('camelCase: ')
snake = []

for i in camel:
    if i.isupper():
        snake.append('_')
        snake.append(i.lower())
    else:
        snake.append(i)

print('snake_case: ' + ''.join(snake))

