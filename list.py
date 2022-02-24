# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
#                      "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
#                      "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#                      "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
#                      "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
#                      "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
#                      "New Mexico", "Arizona", "Alaska", "Hawaii"]
# num_of_state = len(states_of_america)
# print (states_of_america[num_of_state-1])
# import random
#
# names_string = input("give me evreybosy names, separated by a comma.")
# names =names_string.split(", ")
#
# num_items =len(names)
#
# random_choices = random.randint(0, num_items- 1)
# person_who_will_pay = names[random_choices]
# print("person who will pay the bill"+person_who_will_pay)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][0])
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# horizontal = int(position[0])
# vertical = int(position[1])
# selected_row = map[vertical-1]
# selected_row[horizontal-1] = "x"
# print(f"{row1}\n{row2}\n{row3}")
horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical-1]
selected_row[horizontal-1] = "x"
print(f"{row1}\n{row2}\n{row3}")


