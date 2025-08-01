from random import randint

def main():
    level = get_level()
    guess = get_guess()
    correct = randint(2,level)
    prompt = is_right(guess, correct)
    print(prompt)

def get_level():
    while True:
        try:
            integer = int(input('Level: '))
            if integer > 0:
                return integer
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            integer = int(input('Guess: '))
            if integer > 0:
                return integer
        except ValueError:
            pass

def is_right(x, y):
    if x < y:
        return 'Too small!'
    elif x > y:
        return 'Too large!'
    elif x == y:
        return 'Just right!'

main()
