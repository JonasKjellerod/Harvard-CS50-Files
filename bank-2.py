def main():
    a = input('Greetings ')
    print(f'${value(a)}')

def value(greeting):
    if greeting[:5].lower() == 'hello':
        return 0
    elif greeting[0].lower() == 'h' and greeting[1:5].lower() != 'ello':
        return 20
    else:
        return 100

if __name__ == '__main__':
    main()


