name = input("Type yout name: ")
print(name + ", welcome to this adventure!\n")

answer = input(
    "You just woke up\nYou look around and realise you are on a dirt road\nYou have to find a way back home, you walk straight for a few minutes and then the road ends, you can go left or right. What would you choose? ").lower()

if answer == "left":
    
    q2 = input("You come to a river, do you want to walk around it or swin across?\nType walk to walk around and swim to swim accross: ").lower()

    if q2 == "swin":
            print("\nYou swam acrross and were eaten by an alligator. You lose")
    elif q2 == "walk":
        q3 = input("\nYou walked for many miles, and it got dark. Do you keep walking or sleep in the woods?\nType walk or sleep: ").lower()

        if q3 == "walk":
            print("\nYou are so tired, but you see some lights! You finally made it to the city, now it's just another long walk, but you are going home!")
        elif q3 == "sleep":
           print("\nIn the middle of the night you hear a noise. Oh wait, it is a bear! It's coming at you... You lose")
        else:
            print("\nNot a valid option. You lose!")
    else:
        print("\nNot a valid option. You lose!")

elif answer == "right":
    q4 = input(
        "\nYou come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    
    if q4 =="cross":
       q5 = input(
            "\nYou cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
       if q4 == "yes":
            print("\nThey are actually a forest guard and help you to find the way out. You are going home!")
       elif q5 == "no":
            q6 = input("\nYou keep walking for almost an hour and find a gas station, do you go in? (yes/no) ").lower()

            if q6 == "yes":
                print("\nYou enter and ask for help to get back to the city, the seller gives you a map and you manage to return home.")
            elif q6 == "no":
                print("\nYou keep walking, you think you can get back on your own, but it starts to get dark and you have no food or water. You lose")
            else:
                print('Not a valid option. You lose.')

       else:
            print('Not a valid option. You lose.')

    elif q4 =="back":
        print("\nYou have been walking for hours now and ran out of water. You lose")
    else:
        print("\nNot a valid option. You lose!")
   
else:
    print("\nNot a valid option. You lose!")

print("\nThank you for playing, "+ name + "!\n")