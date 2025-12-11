def main():
    rainfall_list = []
    month = 1

    while month <= 12:
        try:
            rainfall_str = input(f"Enter rainfall for month {month}: ")

            if not rainfall_str:
                raise ValueError
            rainfall = float(rainfall_str)
            if rainfall < 0:
                raise ValueError

            rainfall_list.append(rainfall)
            month += 1

        except ValueError:
            print("Invalid rainfall amount. Please enter a positive number.")

    highest = max(rainfall_list)
    lowest = min(rainfall_list)
    total = sum(rainfall_list)
    average = total / len(rainfall_list)

    print("\nData list:", rainfall_list)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Total:", total)
    print("Average:", average)

main()
