price = 0.99
pounds = float(input("Enter number of pounds: "))
if pounds <= 0:
    print("Error: Pounds must be greater than zero.")
else:
    gross_sales = pounds * price
if pounds>=10000:
        discount_rate = 0.40
elif pounds >=1000:
        discount_rate = 0.30
elif pounds>=100:
        discount_rate = 0.20
elif pounds >= 10:
        discount_rate = 0.10
else:
    discount_rate = 0.0

discount = gross_sales * discount_rate
final_amount = gross_sales - discount

print("Number of pounds:", pounds)
print("Gross sales:",gross_sales)
print("Discount:", discount)
print("Final Amount:", final_amount)
     
