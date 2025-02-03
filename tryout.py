num = input("Vuvedete mnogocifreno chislo: ")
print(tuple(num))
print(tuple(num[::-1]))

k = int(input("Vuvedete broi chisla v lista: "))
s = []
j = k
while k>0:
    h = input("Vuvedete chislo: ")
    s.append(h)
    k = k-1
print(s)
a=1
d=0
x=1
while j>1:
    s.insert(a, int(s[d])+int(s[x]))
    a = a+2
    d = d+2
    x = x+2
    j = j-1
print(s)

text = input("Vuvedete text: ")
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print("Rechnik:", char_count)


n = int(input("Vuvedete cqlo chislo: "))
my_list = list(range(1, n + 1))
my_dict = {key: value for key, value in zip(my_list, my_list[::-1])}
print("Rechnik:", my_dict)