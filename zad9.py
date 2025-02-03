def tpls():
    numbers = input("Въведете числа, разделени със ' '.    ")
    numbers1 = numbers.split(" ")
    suma = 0
    suma1 = 0
    tpl = tuple(numbers1)
    for i in tpl:
        if i.isnumeric():
            suma1+=1
            k = int(i)
            if k%2==0:
                suma+=1
    print("Всички числа са: ",suma1)
    print("Четните числа са: ",suma)
tpls()
