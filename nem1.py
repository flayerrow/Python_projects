number = int(input("which num do u want to check?"))
if number % 2 == 0:
    print("this is a even number")
else:
    print("this is a odd number")
height = int(input("give me your height in cm?"))
if height >=120:
    print("allow for roller coaster")
    age = int(input("what is your age?"))
    if age <12:
        print ("you have to pay 5 dollars")
    elif age < 18:
        print("you have to pay 7 dollars")
    else:
        print("you have to pay 12 dollars")
else:
    print("not allowed for roller coaster")
Height = int(input("give me your height in cm?"))
if Height >= 120:
    print ("you can ride")
    age = int(input("tell me your age?"))
    bill = 0
    if age <=12:
        bill +=5
        print ("you have to pay 5 dollars")
    elif age<18:
        bill +=7
        print("you have to pay 7 dollars")
    elif age >=18:
        bill +=12
        print("you have to pay 12 dollars")
        want_photo = input("want photo just type", "Yes or No")
        if want_photo == "Yes":
            bill += 3
else:
    print("you cannot ride")