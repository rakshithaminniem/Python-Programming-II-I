import math

print("╔══════════════════════════╗")
print("║      🧮 CALCULATOR       ║")
print("╚══════════════════════════╝")

print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Remainder")
print("7. Square Root")

choice = int(input("\nEnter your choice (1-7): "))

if choice == 7:
    num = float(input("Enter a number: "))

    if num < 0:
        print("❌ Square root of a negative number is not possible!")
    else:
        result = math.sqrt(num)
        print("\n━━━━━━━━━━━━━━━━━━━━")
        print(f"   √{num:g} = {result:g}")
        print("━━━━━━━━━━━━━━━━━━━━")

else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = num1 + num2
        symbol = "+"

    elif choice == 2:
        result = num1 - num2
        symbol = "-"

    elif choice == 3:
        result = num1 * num2
        symbol = "×"

    elif choice == 4:
        if num2 == 0:
            print("❌ Cannot divide by zero!")
            exit()
        result = num1 / num2
        symbol = "÷"

    elif choice == 5:
        result = num1 ** num2
        symbol = "^"

    elif choice == 6:
        result = num1 % num2
        symbol = "%"

    else:
        print("❌ Invalid choice!")
        exit()

    print("\n━━━━━━━━━━━━━━━━━━━━")
    print(f"   {num1:g} {symbol} {num2:g} = {result:g}")
    print("━━━━━━━━━━━━━━━━━━━━")