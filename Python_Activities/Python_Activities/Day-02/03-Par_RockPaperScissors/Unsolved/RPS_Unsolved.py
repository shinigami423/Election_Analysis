# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (user_choice == 'r' and computer_choice == "r"):
    print("computer chose rock")
    print("You tie")

elif (user_choice == 'r' and computer_choice == "p"):
    print("computer chose paper")
    print("You lose")

elif (user_choice == 'r' and computer_choice == "s"):   #rock
    print("computer chose scissors")
    print("You win")

elif (user_choice == 'p' and computer_choice == "p"):
    print("computer chose paper")
    print("You tie")

elif (user_choice == 'p' and computer_choice == "s"):
    print("computer chose scissor")
    print("You lose")
    
elif (user_choice == 'p' and computer_choice == "r"):    #paper
    print("computer chose paper")
    print("You win")

elif (user_choice == 's' and computer_choice == "p"):
    print("computer chose paper")
    print("You win")

elif (user_choice == 's' and computer_choice == "s"):
    print("computer chose scissor")
    print("You tie")
    
elif (user_choice == 's' and computer_choice == "r"):     #scissor
    print("computer chose paper")
    print("You lose")

else:
    print("Please try again")