import datetime
def kasova_belejka():
    prices = list()
    counts = list()
    sums = list()
    print("Въведете информация за стоките.")
    print("Въведете код '00' за издаване на бележка.")
    print("-------------------------------")
    while True:
        code = input("Въведете код на стока: ")
        suma=0
        if code == "00":
            print("-------------------------------")
            print("-------------------------------")
            for i in range(len(prices)):
                print("             ", counts[i],"бр"," X ", prices[i],"лв ", "=", f'{sums[i]:.2f}',"лв")
                print("-------------------------------")
                suma+=sums[i]
            print("             Обща сума: ", f'{suma:.2f}', "лв")
            money = float(input("             Дадена сума: "))
            change = money-suma
            if change<0:
                x = datetime.datetime.now()
                print("             Недостатъчна сума.")
                print("             Не достигат: ", f'{(suma-money):.2f}', "лв")
                print("             Дата/Час: ",x.strftime("%c"))
            else:
                x = datetime.datetime.now()
                print("             Ресто: ", f'{change:.2f}', "лв")
                print("             Дата/Час: ", x.strftime("%c"))
            break
        price = float(input("Въведете цена на стока: "))
        prices.append(price)
        count = int(input("Въведете брой стоки: "))
        counts.append(count)
        summ = price*count
        sums.append(summ)
kasova_belejka()


