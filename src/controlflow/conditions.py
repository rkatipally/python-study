def simpleIf():
    late = True
    if late:
        print("This is true")
    else:
        print("this is not true")

def showElf():
    n = 1000
    if n < 1000:
        print("n is less than 10000")
    elif n > 500:
        print(" n is greater than 500")
    else:
        print("n is less than 500")

def showTernary():
    total = 100
    discount = 25 if total > 100 else 0
    print(discount)
simpleIf()
showElf()
showTernary()