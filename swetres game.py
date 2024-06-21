#Swetres Game

# This line imports the random module to generate random number.
import random
# This line prints welcome message  to the user.
print("Welcome to the Swetres Game!")       
# This line generates 3 winning combination number betweeen 0-9.
winning_combination = [random.randint(0, 9) for _ in range(3)]    
# This line initialize an empty list to store the user combination.            
user_combination = []                                                  
# This line collects user input.
for i in range(3):                                                     
    elements = input("Enter your swetres number: ")
    user_combination.append(elements)
# This line check if user combination is win or lose.
print(user_combination)
if user_combination == winning_combination:
    print("Congratulations! daog ka!")
else:
    print(f"Sorry, patad nasab sunod. The winning combination is: {winning_combination}")
