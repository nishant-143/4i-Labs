import random
lis = ['rock','paper','scissors']
my_choice = input("Enter rock, paper, or scissors: ")
computer_choice = random.choice(lis)
if my_choice not in lis:
    print("Invalid choice")
else:
    print("computer's choice:",computer_choice)
    if((my_choice == 'rock' and computer_choice == 'scissors') or (my_choice == 'paper' and  computer_choice == 'rock') or (my_choice == 'scissors' and  computer_choice == 'paper')):
        print("you win!")
    elif(my_choice == computer_choice):
        print("it's a draw")
    else:
        print("you lose!")               