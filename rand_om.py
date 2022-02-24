# import random
#
# random_integer = random.randint(1,10)
# print(random_integer)
# randomFloat  = random.random() *5
# print(randomFloat)
# love_score = random.randint(1,100)
# print(f"your love score is{love_score}")
# import random
# random_integer = random.randint(0,1)
# print(random_integer)
# random_float = random.random()*5
# print(random_float)
# love_score = random.randint(1,100)
# print(f"your love score is {love_score}")
# fruits = ["apple", "peach", "pear"]
# # for fruit in fruits:
#     # print(fruit)
#     # print(fruit + "pie")
# print(fruits)
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# # total_height = 0
# # for height in student_heights:
# #     total_height +=height
# # print(total_height)
# #
# # number_of_students = 0
# # for student in student_heights:
# #     number_of_students += 1
# # print(number_of_students)
# # average_heights = round(total_height / number_of_students)
# # print(average_heights)
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students +=1
# print(number_of_students)
#
# average_students = round(total_height/number_of_students)
# print(average_students)
# student_scores = input("give me a student score list")
# for n in range(0, len(student_scores)):
#    student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# print(min(student_scores))
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# print(min(student_scores))
# highest_score =0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#         print(f"your hightset score is",{highest_score})
# total = 0
# for number in range(1,101):
#     total += number
# print(total)
# total = 0
# for number in range(2, 101,2):
# #     total += number
# # print(total)
# total =0
# for number in range(0,101):
#     if number % 2 == 0:
#         total += number
# print(total)
for number in range(0,101):
    if number% 3 ==0 and number % 5 ==0:
        print("fizzbuzz")
    elif number % 3 ==0:
        print("fizz")
    elif number %5 == 0:
        print("buzz")
    else:
        print(number)