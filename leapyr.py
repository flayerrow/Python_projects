print(" is it is a leap year")
year = int(input("give a year you want to check?"))
if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("its a leap year")
        else:
            print("its not a leap year")
    else:
        print("it is aleap year")
else:
    print("its not a leap year")



