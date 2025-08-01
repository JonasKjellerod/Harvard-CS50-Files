def main():
    a = convert(input('Fraction: '))
    print(gauge(a))



def convert(prompt):
    while True:
        try:
            fraction = prompt.split('/')
            x = int(fraction[0])
            y = int(fraction[1])
            if x/y <= 1:
                return round((x/y)*100)
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError

def gauge(x):
    if 1 < x < 99:
        return f'{x}%'
    elif 1 >= x:
        return 'E'
    elif 99 <= x:
        return 'F'

if __name__ == '__main__':
    main()
