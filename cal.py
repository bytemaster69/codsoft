import time
from colorama import Fore, Style

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero."

def display_loading_animation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.3)
    print(Style.RESET_ALL)

def calculator():
    print(Fore.CYAN + "Simple Calculator" + Style.RESET_ALL)

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter numeric values." + Style.RESET_ALL)
        return

    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
        return

    if choice not in range(1, 5):
        print(Fore.RED + "Invalid choice. Please choose a number between 1 and 4." + Style.RESET_ALL)
        return

    print(Fore.YELLOW + "\nCalculating", end="")
    display_loading_animation()

    if choice == 1:
        result = add(num1, num2)
        operation = "Addition"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == 4:
        result = divide(num1, num2)
        operation = "Division"

    print(Fore.GREEN + f"\n{operation} Result: {result}" + Style.RESET_ALL)

if __name__ == "__main__":
    calculator()
