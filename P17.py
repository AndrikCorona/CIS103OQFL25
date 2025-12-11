import random

def powerball():
    nums = []
    while len(nums) < 5:
        n = random.randint(1, 69)
        if n not in nums:
            nums.append(n)
    nums.sort()
    print("Powerball:", nums)

def mega_million():
    nums = []
    while len(nums) < 5:
        n = random.randint(1, 70)
        if n not in nums:
            nums.append(n)
    nums.sort()
    print("Mega Million:", nums)

def lucky_day():
    nums = []
    while len(nums) < 5:
        n = random.randint(1, 45)
        if n not in nums:
            nums.append(n)
    nums.sort()
    print("Lucky Day Lotto:", nums)

def lotto():
    nums = []
    while len(nums) < 6:
        n = random.randint(1, 52)
        if n not in nums:
            nums.append(n)
    nums.sort()
    print("Lotto:", nums)

def main():
    choice = 0
    
    while choice != 9:
        print("\n--- Illinois Lottery Menu ----")
        print("1. Powerball")
        print("2. Mega Million")
        print("3. Lucky Day Lotto")
        print("4. Lotto")
        print("9. Quit")
        
        user = input("Select a game: ")
        
        if not user.isdigit():
            print("Invalid menu selection")
            continue
        
        choice = int(user)
        
        if choice == 1:
            powerball()
        elif choice == 2:
            mega_million()
        elif choice == 3:
            lucky_day()
        elif choice == 4:
            lotto()
        elif choice == 9:
            break
        else:
            print("Invalid menu selection")
        
        input("Hit enter key to return to menu")

main()
