import random
import time


def stringModify(str):
    model = "Hello <<UserName>>, How are you?"
    model = model.replace("<<UserName>>", str, 1)
    return model


def headtail(count):
    head = 0
    tails = 0
    for x in range(count):
        number = random.randint(0, 1)
        if number == 0:
            head = head + 1
        else:
            tails = tails + 1

    print("head is " + str((head * 100 / count)))
    print("tails is " + str((tails * 100 / count)))

    return


def leapyear(year):
    year = str(year)
    if year[2] == '0' and year[3] == '0':
        year = int(year)
        if year % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        year = int(year)
        if year % 4 == 0:
            print("leap year")
        else:
            print("not a leap year")
    return


def two_table(n):
    count = 1
    ref = 0
    while int(n) >= int(ref):
        print(count)
        count = count * 2
        ref = ref + 1
    return


def harmonic_sum(N):
    first = 1
    second = 1
    third = 1
    fourth = 2
    ref = 1
    while int(N) > int(ref):
        first = first * fourth + second * third;
        second = second * fourth;
        fourth = fourth + 1;
        ref = ref + 1

    print(first)
    print(second)

    return


def gambler(stack, goal, number):
    number = int(number)
    stack = int(stack)
    goal = int(goal)
    while (number > 0):
        win = 0
        loss = 0
        count = 0
        value = stack
        while (value > 0 and value < goal):
            coin = random.randint(0, 1)
            if (coin == 0):
                win = win + 1
                value = value + 1
            else:
                loss = loss + 1
                value = value - 1
            count = count + 1
        print("Win Percentage is " + str(((win * 100) / count)))
        print("loss Percentage is " + str(((loss * 100) / count)))
        number = number - 1

    return


def random_numbers(N):
    myset = set()
    count = 0
    while len(myset) < int(N):
        number = random.randint(1, 10000000)
        myset.add(number)
        count = count + 1

    print(myset)
    return


def timex():
    x = input("Press any key to start ")
    start = time.time()
    y = input("Press any key to stop ")
    end = time.time()
    print(end - start)
    return


def tictoe():
    a = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    printarray(a)
    totalchance=9
    chance=True
    while totalchance > 0 :
        if(chance == True):
            userchance(a)

       totalchance=totalchance-1
    return

def printarray(a):

    for x in a:
     print(x)
    return

def userchance(a):
    no = input("Enter no to mark ")


def checkemptyplace(no,a):

    switcher = {

        1: a[0][0],
        2: a[0][1],
        3: a[0][2],
        4: a[1][0],
        5: a[1][1],
        6: a[1][2],
        7: a[2][0],
        8: a[2][1],
        9: a[2][2]
    }

    tempvar=switcher.get(int(no),"noting")

    tempvar=str(tempvar)
    if tempvar=='x' or tempvar == 'o':


    




