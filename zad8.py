import math
def square():
    a = int(input("Страна: "))
    s = a*a
    p = 4*a
    print("Лице: ",s, "    Периметър: ", p)

def rectangle():
    a = int(input("Страна1: "))
    b = int(input("Страна2: "))
    s = a*b
    p = 2*(a+b)
    print("Лице: ",s, "    Периметър: ", p)

def triangle():
    a = int(input("Най-дълга страна: "))
    b = int(input("Страна2: "))
    c = int(input("Страна3: "))
    if a+b>c:
        p = a+b+c
        k = p/2
        s = math.sqrt(k*(k-a)*(k-b)*(k-c))
        print("Лице: ",s, "    Периметър: ", p)
    else:
        print("Невъзможен триъгълник")

def trapezoid():
    a = int(input("Основа1: "))
    b = int(input("Основа2: "))
    c = int(input("Страна1: "))
    d = int(input("Страна2: "))
    h = int(input("Височина: "))
    s = (a+b)*h/2
    p = a+b+c+d
    print("Лице: ",s, "    Периметър: ", p)\

def invalid():
    print("Невалидна фигура")

figure = input("Въведете една от фигурите: 'square', 'rectangle', 'triangle', 'trapezoid': ")
figure.replace(" ","").lower()
if figure == "square":
    square()
elif figure == "rectangle":
    rectangle()
elif figure == "triangle":
    triangle()
elif figure == "trapezoid":
    trapezoid()
else:
    invalid()

