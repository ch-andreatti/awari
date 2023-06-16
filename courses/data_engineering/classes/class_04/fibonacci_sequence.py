
def fibonacci_sequence(limit: int, fibonacci_list: list = [0, 1]):

    # Base case
    if limit in fibonacci_list:
        return fibonacci_list
    
    new_value = fibonacci_list[-1] + fibonacci_list[-2]
    if new_value > limit:
        return fibonacci_list

    # Recursion
    fibonacci_list.append(new_value)
    return fibonacci_sequence(limit, fibonacci_list)

user_input = int(input("Number input: "))
print(fibonacci_sequence(user_input))
