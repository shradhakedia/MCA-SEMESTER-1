def main():
    import random
    print("Welcome to Stone Paper Scissor Game!!\nThere are 3 rounds in this Game\nLet's start")
    choices=["stone","paper","scissor"]
    try:
        n,userscore,compscore=3,0,0
        while(n>0):
            userchoice=input("Enter stone or paper or scissor\nEnter your Choice:")
            compchoice=random.choice(choices)
            print("Your Opponent choice is:",compchoice)
            if userchoice=="stone":
                if compchoice=="paper":
                    compscore+=1
                    print("You lost in this round")
                elif compchoice=="scissor":
                    userscore+=1
                    print("You won in this round")
                else:
                    print("No Winner in this round")
            elif userchoice=="paper":
                if compchoice=="scissor":
                    compscore+=1
                    print("You lost in this round")
                elif compchoice=="stone":
                    userscore+=1
                    print("You won in this round")
                else:
                    print("No Winner in this round")
            elif userchoice=="scissor":
                if compchoice=="stone":
                    compscore+=1
                    print("You lost in this round")
                elif compchoice=="paper":
                    userscore+=1
                    print("You won in this round")
                else:
                    print("No Winner in this round")
            else:
                print("Invalid Input!!")
            n-=1
            print("      SCORE BOARD\nYour Score\tOpponent's Score\n",userscore,"\t\t\",compscore)
        print("FINAL RESULT:")
        if userscore>compscore:
            print("Congratulations!,You won! with the score of",userscore)
        elif userscore==compscore:
            print("Its a Tie")
        else:
            print("Oops,Game Over!!,You Lost")
    except Exception as e:
        print("Invalid Input!!!")
if __name__=="__main__":
    main()