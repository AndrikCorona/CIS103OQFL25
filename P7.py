def miles_to_kilometers(miles):
    kilometers = miles * 1.609344
    return kilometers


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def pounds_to_kilograms(pounds):
    kilograms = pounds *0.45359237
    return kilograms


miles =float(input("Enter distance in miles: "))
km = miles_to_kilometers(miles)
print("Distance in kilometers:", km)

pounds = float(input("\nEnter weight in pounds:"))
kg = pounds_to_kilograms(pounds)
print("Weight in kilograms:", kg)

fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print("Temperature in Celsius:", celsius)
