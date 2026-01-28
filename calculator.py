def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, ** (for exponentiation)")
    print("Type 'quit' to exit.")
    
    while True:
        try:
            expression = input("Enter expression (e.g., 2 + 3): ")
            if expression.lower() == 'quit':
                break
            result = eval(expression)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print(f"Error: Invalid input ({e})")

if __name__ == "__main__":
    calculator()