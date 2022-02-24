# # result = 8/2
# # result /= 2
# # print(result)
# score = 0
# height =1.8
# iswinning =True
#
# #user scores apoint
# # score -= 1
# # print (score)
# printf"your score is{score} ")
Current_age= input("what is your age?\n")
print(Current_age)
age_as_int =int(Current_age)
Years_remaining = 100 - age_as_int
months_remaining =12* Years_remaining
weeks_remaining =52 *Years_remaining
days_remaining = 365 *Years_remaining
message = f"\n you have {days_remaining} Days,{months_remaining} Months and {weeks_remaining} Weeks left"
print(message)
