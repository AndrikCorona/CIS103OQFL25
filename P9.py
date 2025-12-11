def acres_to_hectares(a):
    hectares = a * 0.40487
    return hectares

def quarts_to_liters(q):
    liters = q * 0.946353
    return liters

def fahrenheit_to_kelvin(f):
    kelvin = (f - 32) * (5/9) + 273.15
    return kelvin

again = "y"

while again.lower() == "y":
    print("Conversion Program")

    try:
        acres = float(input("Enter acres: "))
        if acres < 0:
            print("Input error - acres")
        else:
            print(acres, "converts to", acres_to_hectares(acres), "hectares")
    except:
        print("Input error - acres")

    print("")

    try:
        quarts = float(input("Enter quarts: "))
        if quarts < 0:
            print("Input error - quarts")
        else:
            print(quarts, "converts to", quarts_to_liters(quarts), "liters")
    except:
        print("Input error - quarts")

    print("")

    try:
        fahrenheit = float(input("Enter Fahrenheit: "))
        print(fahrenheit, "converts to", fahrenheit_to_kelvin(fahrenheit), "kelvin")
    except:
        print("Input error - Fahrenheit")

    print("")
    again = input("again y/n? ")
    print("")

print("--done--")
