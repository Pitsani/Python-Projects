start_of_year = input("Code in start of year (devided by ','): ").split(',')
end_of_year = input("Code in end of year(devided by ','): ").split(',')
list_start = list()
list_end = list()
if not start_of_year or not end_of_year:
    print("no data")
else:
    for i in start_of_year:
        list_start.append(i)
    for i in end_of_year:
        list_end.append(i)
    print(list_start)
    print(list_end)
    left_count = 0
    new = 0
    for i in list_start:
        if i not in list_end:
            left_count +=1 
    for i in list_end:
        if i not in list_start:
            new +=1
    print(left_count)
    print(new)
    total_employees = len(list_start) - left_count + new
    turnover_rate = (left_count / total_employees) * 100
    print(f"Percent of turnover: {100-turnover_rate:.2f}%")
  