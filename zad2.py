def set_gen(numbers):
    result_set = set()
    for num in numbers:
        count = numbers.count(num)
        for i in range(1, count + 1):
            result_set.add(str(num) * i)
    return result_set
numbers_list = [4,4,4]
result = set_gen(numbers_list)
print(result)
