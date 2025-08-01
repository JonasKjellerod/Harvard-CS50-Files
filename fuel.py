def main():
    a = get_fraction('Fraction: ')
    if 1 < a < 99:
        print(f'{a}%')
    elif 1 >= a:
        print('E')
    elif 99 <= a:
        print('F')



def get_fraction(prompt):
    while True:
        try:
            fraction = input(prompt).split('/')
            x = int(fraction[0])
            y = int(fraction[1])
            if x/y <= 1:
                return round((x/y)*100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()
