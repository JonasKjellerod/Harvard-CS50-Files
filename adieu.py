import inflect

def main():
    p = inflect.engine()
    list_of_names = []
    while True:
        try:
            list_of_names.append(input('Name: '))
        except EOFError:
            print()
            break


    print('Adieu, adieu, to', p.join(list_of_names))




main()
