n = int(input("n = "))
k = list()
p = list()
suma=0
g=0
d=0
if 15<n<35:
    for i in range(n):
        l = int(input("Number: "))
        if 30<=l<=300:
            k.append(l)
    for i in k:        
        if (i%100)//10%3==0:
            suma+=1
        if i%6==4:
            p.append(i)
    print("First list: ",k)
    print("Count of numbers which decimals can devide by 3: ", suma)
    z = min(p)
    print("Index of minimal number that %6==4 is TRUE: ",k.index(z))
    p.clear()
    for i in k:
        if 9<i<100 and (i%2==0 or i%3==0):
            p.append(i)
    for i in p:
        if p.index(i)%2==1:           
            g += i
            d += 1
    print("Second list: ",p)
    print("Average of numbers which indexes are odd: ",g/d)
    f = min(p)
    p.remove(f)
    print("Second list without minimal number:", p)
else:
    print("The input must be a number between 15 and 35.")
