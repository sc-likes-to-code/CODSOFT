import random

print("********** Rock-Paper-Scissors Game **********")

c=True
a=1
us=0
cs=0

while(c==True):
    ch=input("Enter R/r for Rock or P/p for Paper or S/s for Scissors: ").upper()
    
    if(ch!='R' and ch!='P' and ch!='S'):
        print("Invalid input")

    else:
        print("Round ", a, ":")
        a+=1
        cci=random.randrange(1,15)
        
        if (1<=cci<=5) :
            cc='R'
        elif (6<=cci<=10):
            cc='P'
        elif (11<=cci<=15):
            cc='S'
        
        print("User\'s choice: ", ch, "			", "Computer\'s choice: ", cc)
        
        if (ch=='R' and cc=='S') or (ch=='P' and cc=='R') or (ch=='S' and cc=='P'):
            print("The user wins!!\nCongratulations!! ")
            us+=1
            co=input("Do you want to continue? (Y or y for yes, N or n for no): ")
            if (co=='Y' or co=='y'):
                c=True
            else:
                c=False
                print("Thanks for playing!! ")

        elif (ch==cc):
            print("It's a tie!! ")
            co=input("Do you want to continue? (Y or y for yes, N or n for no): ")
            if (co=='Y' or co=='y'):
                c=True
            else:
                c=False
                print("Thanks for playing!! ")

        else:
            print("The user lost!!\nBetter luck next time!! ")
            cs+=1
            co=input("Do you want to continue? (Y or y for yes, N or n for no): ")
            if (co=='Y' or co=='y'):
                c=True
            else:
                c=False
                print("Thanks for playing!! ")

        print("User\'s score: ", us)
        print("Computer\'s score: ",cs)

print("**********Thanks for playing!!!**********")
