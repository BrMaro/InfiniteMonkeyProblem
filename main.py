import random

txt = input("Enter words or phrases: ")
def wordGen(n):
    rnd = random.choices(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', ' '], k=n)
    rndm = ''.join(rnd)
    return rndm


def score(goal, testString):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == testString[i]:
            numSame += 1

    return numSame / len(goal)


def infiniteMonkey(str):
    count = 0
    while True:
        best = 0
        wordTest = wordGen(len(str))
        if score(str, wordTest) > best:
            best = score(str, wordTest)
            print(wordTest)
        count = count + 1
        if wordTest == str:
            print(count)
            break


infiniteMonkey(txt)