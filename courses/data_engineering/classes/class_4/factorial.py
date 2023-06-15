
def factorial_recursion(num: int) -> int:
    
    # Base case
    if num in [0, 1]:
        return num
    
    # Recursion
    return num * factorial_recursion(num - 1)

def factorial(num: int) -> int:

    result = 1
    for number in range(1, num + 1):
        result *= number
    
    return result

user_input = int(input("Number input: "))

try:
    print(factorial_recursion(user_input))
except RecursionError:
    print(factorial(user_input))