def chars():
    text = input("Enter text: ")
    tuples = tuple(text)
    dicts = {}
    for i in tuples:
        sum = tuples.count(i)
        dicts[i] = sum
    print(dicts)
chars()
