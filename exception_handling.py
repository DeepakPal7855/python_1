def divide_numbers(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        print(f"the result of {a} divided by {b} is {result}.")
    finally:
        print('Execution of try-except finally block is complete.')
    return result


num1 = 10
num2 = 0
output = divide_numbers(num1, num2)
print(f'Result of division:{output}')
