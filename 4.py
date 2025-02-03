def numbers():
    k = list()
    l = list()
    while True:
        try:
            n = int(input("Число: "))
            if n!=0:
                if n%3==0 and n%2==0:
                    k.append(n)
                if n%7==0 and n%2==1:
                    l.append(n)            
            else:
                break                               
        except ValueError:
                print("Въведете цяло число.")
    suma = 0
    for i in range(len(k)):
        if i%2==1:
            suma+=k[i]
    j = max(l)
    u = min(l)
    z = j*u
    print(k)
    print(l)
    l.sort(reverse=True)
    print("Сума на елементи с нечетен индекс от първи списък:", suma)
    print("Втори списък в низходях ред: ", l)
    print("Произведение на минимален и максимален елементи от втори списък:", z)    
numbers()
    
                

            