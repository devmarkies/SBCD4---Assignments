#humpyang game
#p1 = user(real player)
#c1&2 = (computer random attack)

# This line import randint from random module.
from random import randint 
# This line ask for user input.
P1 = int( input("1 - for Fold 0- for Unfold Select your number: "))
# Check if the user inputed assign value.
if P1 not in [0,1]: 
    print("Invalid Selection")
# This line executed if the user inputed is valid.
else:
    C1, C2 = randint(0,1), randint(0,1) # assign value
    selection = "Unfold", "Fold"        # choices from assign value
    results = "Player1 win", "Computer1 win", "Computer2  win", "Draw"   # possible results
    print(f"P1 = {selection[P1]}\nC1 = {selection[C1]}\nC2 = {selection[C2]}\n") # for excuted
    
# This lines is check if who is the winner between the user and computers.
    if P1 != C1 and P1 != C2:
        print(results[0])
    elif C1 != P1 and C1 != C2:
        print(results[1])
    elif C2 != P1 and C2 != C1:
        print(results[2])
    else:
        print(results[3])