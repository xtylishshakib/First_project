import random

l = ["rock", "scissor", "paper"]

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
    Game start....
    1 Yes
    2 No | Exit
    '''))

    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
            1 Rock
            2 Scissor
            3 Paper
            '''))

            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            else:
                print("Invalid choice, try again")
                continue

            cchoice = random.choice(l)

            print("computer value:", cchoice)
            print("user value:", uchoice)

            if cchoice == uchoice:
                print("Game Draw")
                ucount += 1
                ccount += 1
            elif (uchoice == "rock" and cchoice == "scissor") or (uchoice == "paper" and cchoice == "rock") or (
                    uchoice == "scissor" and cchoice == "paper"):
                print("You Win")
                ucount += 1
            else:
                print("Computer Wins")
                ccount += 1

        print("\nFinal Scores:")
        print("User Score:", ucount)
        print("Computer Score:", ccount)
        if ucount > ccount:
            print("Congratulations! You are the overall winner!")
        elif ccount > ucount:
            print("The computer wins overall. Better luck next time!")
        else:
            print("It's a draw overall!")
    else:
        break
