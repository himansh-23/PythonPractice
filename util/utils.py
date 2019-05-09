import random

def stringModify(str):
    model = "Hello <<UserName>>, How are you?"
    model=model.replace("<<UserName>>", str, 1)
    return model;

def headtail(count):
    head = 0
    tails = 0
    for x in range(count):
        number = random.randint(0, 1)
        if(number == 0):
            head = head+1
        else :
            tails = tails+1

    print("head is " + str((head*100/count)))
    print("tails is " + str((tails*100/count)))

    return

def leapyear(year):

    year = str(year)
    if(year[2]=='0' and year[3] =='0'):
        year = int(year)
        if( year%400 == 0):
            print("leap year")
        else:
            print("not a leap year")
    else:
        year = int(year)
        if(year % 4 == 0):
            print("leap year")
        else:
            print("not a leap year")
    return

def two_table(n):
        count = 1
        ref = 0
        while int(n)>= int(ref):
            print(count)
            count=count*2
            ref=ref+1
        return

def harmonic_sum(N):
     first = 1
     second =1
     third = 1
     fourth = 2
     ref=1
     while int(N) >int(ref):
            first=first*fourth+second*third;
            second=second*fourth;
            fourth=fourth+1;
            ref=ref+1

     print(first)
     print(second)

     return




