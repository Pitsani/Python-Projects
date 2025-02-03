def product_with_list():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    result = 1
    for num in numbers:
        result *= num
    return result
print("Product with list input:", product_with_list())

def product_with_variable_args(*args):
    result = 1
    for num in args:
        result *= num
    return result
result1 = product_with_variable_args(2, 3, 4)
result2 = product_with_variable_args(5, 6)
print("Product with variable args:", result1, result2)

def product_without_params():
    return product_with_variable_args()
result3 = product_without_params()
print("Product without params:", result3)

def Funct(numbers=(1,)):
    result = product_with_variable_args(*numbers)
    return 0.5 * result
funct_result1 = Funct((2, 3, 4))
funct_result2 = Funct((5, 6))
print("Funct results:", funct_result1, funct_result2)
