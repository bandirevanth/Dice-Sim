# Modules
import random

print("""
========== Dice Simulator ==========
[1] Info
[2] Play
[3] Quit
====================================
""")

while True:
    option = int(input("Option: "))
    if option == 1:
        print("""
        App Info:
        Developer - Bandi Revanth
        Version -  1.0 [Console]
        """) 

    if option == 2:
        user = input("Username: ")
        print(f"""      
        White Dice  >>> Luck x2
        Black Dice  >>> Luck x4
        Red Dice    >>> Luck x6
        Orange Dice >>> Luck x8
        \n""")

        dices = ["White Dice", "Black Dice", "Red Dice", "Orange Dice"]

        user_dice = random.choice(dices)
        print(f"Your Dice: {user_dice}")

        comp_dice = random.choice(dices)
        print(f"Computer's Dice: {comp_dice}")     

        choice_roll = input("Roll?(Yes/No): ")

        if choice_roll == "No".lower():
            break
        elif choice_roll == "Yes".lower():
            rand_user = random.randint(1, 6)
            print(f"You Got: {rand_user}")

            rand_comp = random.randint(1, 6)
            print(f"Computer Got: {rand_comp}\n")
            
            if rand_user > rand_comp:
                print(f"{user} Won!")
            elif rand_comp > rand_user:
                print(f"Computer Won!")
            elif rand_comp == rand_user or rand_user == rand_comp:
                print("It's a Tie!")    
        else:
            break        

    if option == 3:
        break
