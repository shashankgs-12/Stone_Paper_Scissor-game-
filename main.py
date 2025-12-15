#Stone paper Scissors game 
'''
(s)stone = 1
(p)paper = -1
(C)scissor = 0
'''
import random
print("s:stone, p:paper, c:scissor")
computer = random.choice([1,-1,0])
youStr=input("Enter your choice: ")
youDict={"s":1,"p":-1,"c":0}
reverseDict={1:"stone",-1:"paper",0:"scissors"}
you=youDict[youStr]
print(f"you choosed {reverseDict[you]}\ncomputer choosed {reverseDict[computer]}")

if(computer==you):
    print("It's Draw")
else:
    if(computer==1 and you==-1):
        print("You won")
    elif(computer==1 and you==0):
        print("you loose")
    elif(computer==-1 and you==1):
        print("you loose")
    elif(computer==-1 and you==0):
        print("you won")
    elif(computer==0 and you==1):
        print("you won")
    elif(computer==0 and you==-1):
        print("you loose")
    else:
        print("something went wrong!")