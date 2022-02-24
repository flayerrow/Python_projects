# states_of_america = ["delware", "spain", "random"]
# states_of_america[1] = "diwakar"
# states_of_america.extend(["himanshu", "shubham"])
# print(states_of_america)
# import random
# names_string = input("give me everybody name, separeted by a comma. ")
# name = names_string.split(", ")
# num_items = len(name)
# random_choice= random.randint(0, num_items -1)
# person_who_will_pay = name[random_choice]
# print(f"who will pay",{person_who_will_pay})
import random
names_string = input("give me everybody names, separetd by acomma. ")
name = names_string.split(", ")
num_int = len(name)
random_choice = random.randint(0,num_int-1)
choi_ce = name[random_choice]
print(" person who will pay " + choi_ce)


