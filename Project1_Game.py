### Adventure Game
name: str = input("Greetings! Type your name: ")
print(name)  # output get by typing user name
print("Hello! " + name + "  Welcome to my game challenge!")
print("Hello", name, "Welcome to my game challenge!")

should_we_play = input("Do you want to play? ").lower()
##Conditionals / Condition(True or False) # = is sign of operator
play = should_we_play == "yes"  # output  yes = True & no = False
should_we_play = input("Do you want to play? ").lower()

## OPerators(and, or, not)
## not (should_we_play == "y" or should_we_play == "yes")

if should_we_play == "y" or should_we_play == "yes":
    print("we are going to play.")
    print("Truly we are going to play")
elif should_we_play == "YES":
    print("WE ARE GOING TO PLAY.")
elif should_we_play == "Yes":
    print("WE ARE GOING TO PLAY.")
## Option for Game
# weapon = input("choice a weapon (sword / axe):").lower()
direction = input("Where do you want to go? (left/right) ").lower()
if direction == "left":
    print("Okay you went left and obstacle stopped, game over.")
elif direction == "right":
    # print("we went right")
    choice = input(
        "Okay, you now see a bridge, do you want to swim under it or cross it? (swim/cross) "
    ).lower()
    if choice == "swim":
        print("you got eaten by sea animal")
    else:
        print("you found gems and won!")

else:
    print("sorry not valid reply, you skipped.")
# else:
#     print("We are NOT going to play...")
