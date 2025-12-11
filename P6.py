calories_per_minute = 4.33
again= "y"

while again.lower() == "y":
    print("\nCalorie Table Program")
    minutes_input = input("Enter running minutes: ")
    if minutes_input.strip() == "":
        rint("Minutes cannot be blank")
    else:
        try:
            minutes = float(minutes_input)
            if minutes <= 5:
                print("Minutes must be greater than 5")
            else:
                current = 5
                while current <= minutes:
                    calories = current * calories_per_minute
                    print("minutes:", current, "Calories:", round(calories, 2))
                    current += 5

        except:
            print("invalid input. Please enter a number.")
    again = input("Again y/n:")
    print("--------------------")
print("----done----")
