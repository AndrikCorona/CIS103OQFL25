def build_dict():
    return {
        1:"I", 2:"II", 3:"III", 4:"IV",
        5:"V", 6:"VI", 7:"VII", 8:"VIII",
        9:"IX", 10:"X", 11:"XI", 12:"XII",
        13:"XIII", 14:"XIV", 15:"XV", 16:"XVI",
        17:"XVII", 18:"XVIII", 19:"XIX", 20:"XX",
        21:"XXI", 22:"XXII", 23:"XXIII", 24:"XXIV"
    }

def print_dict(d):
    print("\nCurrent Dictionary:")
    for key in sorted(d.keys()):
        print(key, ":", d[key])

def main():
    roman = build_dict()
    again = "y"
    while again == "y":
        print_dict(roman)
        number_loop = 1
        while number_loop == 1:
            num_input = input("Enter decimal number (0 or negative to quit): ")
            if num_input.strip() == "":
                print("Error: input cannot be blank.\n")
                continue
            try:
                number = int(num_input)
            except:
                print("Error: must be a whole number.\n")
                continue

            if number <= 0:
                print("Exiting number loop.\n")
                number_loop = 0
                continue

            if number in roman:
                print("Roman numeral for", number, "is", roman[number], "\n")
            else:
                print("Number not found in dictionary.")
                add = input("Add this number? (y/n): ").lower()

                if add == "y":
                    rn_input = input("Enter Roman numeral: ").upper()
                    if rn_input.strip() == "":
                        print("Error: cannot be blank.\n")
                    elif not rn_input.isalpha():
                        print("Error: must be alphabetic.\n")
                    else:
                        roman[number] = rn_input
                        print("Added!\n")

        again = input("Run program again (y/n): ").lower()

    print("\nFinal Dictionary:")
    print_dict(roman)
    print("Program ended.\n")

main()
