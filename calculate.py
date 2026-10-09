def calculate(operation, a, b):
    if operation == 'add':
        return a + b
    # elif operation == 'subtract':
    #     return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return 'Cannot divide by zero.'
        return a / b
    elif operation == 'power':
        return a ** b
    elif operation == 'modulo':
        if b == 0:
            return 'Cannot divide by zero.'
        return a % b
    elif operation == 'floor_divide':
        if b == 0:
            return 'Cannot divide by zero.'
        return a // b
    else:
        return "Error: Unsupported operation"

# Example usage
if __name__ == "__main__":
    print(calculate('add', 5, 3))            # Output: 8
    print(calculate('subtract', 5, 3))       # Output: 2
    print(calculate('multiply', 5, 3))       # Output: 15
    print(calculate('divide', 5, 3))         # Output: 1.666...
    print(calculate('divide', 5, 0))         # Output: Cannot divide by zero.
    print(calculate('power', 2, 4))          # Output: 16
    print(calculate('modulo', 10, 3))        # Output: 1
    print(calculate('floor_divide', 10, 3))  # Output: 3