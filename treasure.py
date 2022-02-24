print (" Welcome to Treasure Island")
dec_ide = input("left or right")
if dec_ide == "left":
    print("want to swim or wait")
    diwa = input("do u want to ? swim or wait")
    if diwa == "wait":
        print("enter into match")
        doo_r = input("which door do u want to pick? Red , Yellow or Blue")
        if doo_r == 'Red':
            print ("burned by fire Game over")

        elif doo_r == "Yellow":
            print(" you win")

        elif doo_r == "Blue":
            print("eaten by d beasts game over")
        else:
            print ("game over")





    else:
        print("fall into hole, game over")

else:
     print("fall into hole, game over")

