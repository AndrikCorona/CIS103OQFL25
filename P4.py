name=input("Enter Name: ")
account = input("Enter Account Number: ")
payment= input("Enter Payment Amount: ")
if len(name.strip()) ==0:
    name_message = "Name cannot be blank"
elif len(name.strip()) < 3:
    name_message = "Name to short"
elif not name.isalpha():
    name_message = "Name must be alphabetic"
else:
    name_message = "valid"

if len(account.strip()) == 0:
    account_message ="Account number cannot be blank"
elif not account.isdigit():
    account_message ="Account number must be numeric"
elif len(account) !=9:
    account_message = "Account number be 9 digits"
else:
    account_message = "Valid"

if len(payment.strip()) == 0:
    payment_message ="Payment cannot be blank"
else:
    try:
        payment = float(payment)
        if payment < 0:
            payment_message ="Payment cannot be negative"
        elif payment ==0:
            payment_message ="Payment cannot be zero"
        else:
            payment_message ="valid"
    except:
        payment_message ="payment must be numeric"

print()
print("Name:", name, name_message)
print("Account Number:", account, account_message)
print("Payment:", payment, payment_message)
