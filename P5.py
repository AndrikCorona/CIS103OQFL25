print("-- Program start --")
print("Table codes: A = add, S =subtract, M =multiple, D = divide")

code = input("Select table code: ").upper()
num=float(input("Enter number for table: "))

if code == "A":
    print("Add")
    for i in range (1, 11):
        result = num + i
        print(result, "=", num, "+",i)

elif code == "S":
    print("Subtract")
    for i in range(1,11):
        result = num - i
        print(result, "=", num, "-",i)

elif code == "M":
    prnt("Multiply")
    for i in range(1,11):
        result = num * i
        print(result, "=", num, "*", i)

elif code == "D":
    print("Divide")
    for i in range(1,11):
        result = num / i
        print(result, "=", num, "/", i)

else:
    print("Invalid code entered.")
print("--- done ---")
