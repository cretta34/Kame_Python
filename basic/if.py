# if文

age = -20
age_alcohol = 21
if age >= age_alcohol:
    print("You can drink beer!")
else:
    print("You are too young to drink beer")

age_drive = 18
if age >= age_alcohol:
    print("You can drink beer!")
elif age < age_drive:
    print("You cannot even drive")
else:
    print("You are not allowed to drink beer but you can drive only if you have a driver's license")

if not 0 < age < 120:
    print("The value is invalid!!")

# challenge1
balance = 3000000
withdrawal = 1300000

# if balance > withdrawal:
#     balance -= withdrawal
#     print("Your new balance is {}".format(balance))
# else:
#     print("You don't have money")

# challenge2
withdrawal_limit = 1000000

if withdrawal > withdrawal_limit:
    print("The withdrawal limit is {}".format(withdrawal_limit))
elif balance > withdrawal:
    balance -= withdrawal
    print("Your new balance is {}".format(balance))
else:
    print("You don't have money")