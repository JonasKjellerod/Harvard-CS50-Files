

def groceries():
    grocery_list = {}
    while True:
        try:
            a = input()
        except EOFError:
            for i in sorted(grocery_list):
                print(grocery_list[i],i.upper())
            break
        else:
            if a in grocery_list:
                grocery_list[a] += 1
            else:
                grocery_list[a] = 1

groceries()
