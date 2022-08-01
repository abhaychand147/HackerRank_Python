def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    length = len(string)
    for index in range(0, length):
        if string[index] in "AEIOU":
            kevin += length - index
        else:
            stuart += length - index
    if kevin > stuart:
        print("Kevin {}".format(kevin))
    elif kevin < stuart:
        print("Stuart {}".format(stuart))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
