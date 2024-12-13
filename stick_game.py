'''
Name:Anannya Abhi
Date:3/12/24
Python program for sticks game
'''
def num_check(choice,no_of_sticks):
    no_of_stick=no_of_sticks
    if (choice==1)or(choice==3)or(choice==2) and (choice>=no_of_stick):
        no_of_stick=no_of_stick-choice
        return no_of_stick
    else:
        print("Invalid value for sticks")
no_of_sticks =16
player1_try,player2_try=0,0
print("Welcome to game of Sticks!!")
player1=input("Enter Player 1 name: ")
player2=input("Enter Player 2 name: ")
print(f"Sticks remaining:16")
while no_of_sticks>=0:
    if player1_try!=player2_try:
        choice = int(input(f"{player2}, pick 1, 2, or 3 sticks:"))
        no_of_sticks = num_check(choice, no_of_sticks)
        player2_try+=1
        if no_of_sticks > 0:
            print(f"Sticks remaining:{no_of_sticks}")
        else:
            print(f"{player2},pick the last stick and lose the game!")
            break
    else:
        choice=int(input(f"{player1}, pick 1, 2, or 3 sticks:"))
        player1_try+=1
        no_of_sticks=num_check(choice,no_of_sticks)
        if no_of_sticks>0:
            print(f"Sticks remaining:{no_of_sticks}")
        else:
            print(f"{player1},pick the last stick and lose the game!")
            break
        else:
            print(f"{player1},pick the last stick and lose the game!")
            break
