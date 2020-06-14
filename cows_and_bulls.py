def user(nice):
    e = int(nice[0])
    f = int(nice[1])
    g = int(nice[2])
    h = int(nice[3])
    n = [e,f,g,h]
    return n

def run(o,p):
    q = 0
    w = 0
    for i in range (len(o)):
        if o[i] == p[i]:
            q = q+1
        if o[i] in p:
            w = w+1
    w = w-q
    k = [q,w]
    return k

def numb():
    import random
    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    d = random.randint(0,9)
    m = [a,b,c,d]
    return(m)

def check(L):
    while len(L) != 4:
        print("Enter 4 numbers: (no space required) try again:")
        L = input("==")

    while L.isdigit() != True:                           
        print("Enter 4 numbers: (no space required) try again:")
        L = input("==")
    return L

L1 = numb()
yn = "y"
round = 0
while yn == "y":
    round = round+1
    print("Enter 4 numbers: (no space required)")
    INPUT = input("==")

    LL = check(INPUT)

    L2 = user(LL)

    result = run(L2,L1)

    cow = result[0]
    bull = result[1]

    print("There are",cow,"cows and",bull,"bulls.")
    print("You have tried for",round,"times.")
    print("\n")
    giveup = input("Do you want to stop now and see the answer? If so, enter y: ")
    if giveup == "y":
        print(L1[0],L1[1],L1[2],L1[3])
        break
    if cow == 4:
        print("I know you can do it!")
        break
