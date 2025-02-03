def f2():
    number = int(input("Въведете цяло число: "))
    if number == 0:
        print("Числото трябва да не е нула")
    else:
        k = f1(number)
        return k

def f1(x3):
    if x3 == 0:
        y = f2(x3)
        return y
    else:
        y = 4 * x3
        return y

x1 = int(input("Въведете цяло число: "))
print(f1(x1))

