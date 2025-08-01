def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    c1 = condition1(s)
    c2 = condition2(s)
    c3 = condition3(s)
    c4 = condition4(s)

    if c1 == c2 == c3 == c4 == True:
        return True
    else:
        return False

def condition1(str):
    for i in str[:2]:
        if i.isalpha():
            return True
        else:
            return False

def condition2(str):
    if 2 <= len(str) <= 6:
        return True
    else:
        return False

def condition3(str):
    index = 1
    if str[2:].isalpha() or len(str) == 2:
        return True
    else:
        for j in str[2:]:
            index += 1
            if j == '0':
                return False
            elif j.isnumeric() and str[index:].isnumeric():
                return True
            elif j.isnumeric() and str[index:].isnumeric() == False:
                return False

def condition4(str):
    if ' ' in str or '.' in str or ',' in str:
        return False
    else:
        return True




main()
