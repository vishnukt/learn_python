#Just a rock-paper-scissors with Computer

from random import randint
print("Rock - Paper - Scissors\n 1:Rock\t 2:Paper\t 3:Scissors")
print("-"*15)
rps=["Rock","Paper","Scissors"]
rep="y"
while(rep=="y"):
    user=int(input("Enter int of your Choice : "))
    comp=randint(1,3)
    print("Your Choice : ",rps[user-1])
    print("Commputer Choice : ",rps[comp-1])
    if comp==user:
        print("\nIT IS A TIE\n")
    elif((comp==1 and user==2)or(comp==2 and user==3)or(comp==3 and user==1)):
        print("\nYOU WON\n")
    else:
        print("\nYOU LOSE\n")
    rep=input("Enter y to repeat Game : ".lower())
