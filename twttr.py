def main():
    a = input('Input: ')
    print(shorten(a))




def shorten(word):
    list = []
    vowel = ['a','e','i','o','u']
    for i in word:
        if i.lower() not in vowel:
            list.append(i)
    return ''.join(list)

if __name__ == "__main__":
    main()
