def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

print("Simple Calculator")
print("Operations: +, -, *, /")

while True:
    expression = input("\nEnter expression (e.g. 3 + 4) or 'quit' to exit: ").strip()
    if expression.lower() == 'quit':
        print("Goodbye!")
        break
    try:
        parts = expression.split()
        if len(parts) != 3:
            print("Invalid format. Use: number operator number")
            continue
        a, op, b = float(parts[0]), parts[1], float(parts[2])
        if op not in operations:
            print(f"Unknown operator '{op}'. Use +, -, *, /")
            continue
        result = operations[op](a, b)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid numbers. Please try again.")
