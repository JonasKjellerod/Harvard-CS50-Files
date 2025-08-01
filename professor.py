from random import randint


def main():
    level = get_level()
    score = 0

    for i in range(1,11):
        x = generate_integer(level)
        y = generate_integer(level)


        for j in range(1,4):
            answer = int(input(f'{x} + {y} = '))
            if answer == (x + y):
                score += 1
                break
            elif j == 3 and answer != (x + y):
                print(f'{x} + {y} =', x + y)
                break
            else:
                print('EEE')



    print('Score:', score)



def get_level():
    while True:
        try:
            user_level = int(input('Level: '))
            if user_level in (1,2,3):
                return user_level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    elif level == 3:
        return randint(100,999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
