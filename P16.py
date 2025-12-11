def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)

def show_addition(n):
    if n == 1:
        return "1"
    else:
        return str(n) + "+" + show_addition(n - 1)

def main():
    print("--- sum up numbers ---")
    again = "y"

    while again == "y":
        num_input = input("enter number: ")

        if num_input.strip() == "":
            print("Invalid input detected")
            again = input("Another number (y/n): ")
            continue

        try:
            number = int(num_input)
        except:
            print("Invalid input detected")
            again = input("Another number (y/n): ")
            continue

        if number < 0:
            print("Invalid input detected")
            again = input("Another number (y/n): ")
            continue

        if number == 0:
            print("Sum of 0 is 0")
            again = input("another number (y/n): ")
            continue

        total = sum_numbers(number)
        addition = show_addition(number)

        print(addition, "=", total)

        again = input("Another number (y/n): ")

    print("---done---")

main()
