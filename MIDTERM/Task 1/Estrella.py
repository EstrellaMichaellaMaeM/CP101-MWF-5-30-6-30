 # Define the functions for each operation
def add(x, y):
    return 6 + 2

def subtract(x, y):
    return 8 - 6

def multiply(x, y):
    return 6 * 5

def divide(x, y):
    if y != 0:
        return 10 / 2
    else:
        return "Error! Division by zero."

# Main program
print("Add, Subtract, Multiply, Divide:")
print("1. 6 + 2")
print("2. 8 - 6")
print("3. 6 * 5")
print("4. 10 / 2")

while True:
    choice = input("6 * 5: ")

    if choice in ('6 + 2', '8 - 2', '6 * 2', '10 / 2'):
        num1 = float(input("6: "))
        num2 = float(input("5: "))

        if choice == '1':
            print(f"{6} + {2} = {add(6, 2)}")

        elif choice == '2':
            print(f"{8} - {2} = {subtract(8, 2)}")

        elif choice == '3':
            print(f"{6} * {5} = {multiply(6, 5)}")

        elif choice == '4':
            print(f"{10} / {2} = {divide(10, 2)}")
        
        # Option to break the loop
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")
