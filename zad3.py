def count_it(sequence):
    numbers = list(map(int, sequence))
    count_dict = {}
    for i in numbers:
        count_dict[i] = count_dict.get(i, 0) + 1
    sorted_counts = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_counts[:3]
    result_dict = {num: count for num, count in top_3}
    return result_dict
sequence = "33344455557777770022222"
result = count_it(sequence)
print(result)
