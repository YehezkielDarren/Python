import random
import os
print("Russian Roullete")
print("Win or Go Home :D")
lives=5
while lives!=0:
    print(f"Your HP is {lives} left")
    user_input=int(input("Input A Number At Range 1-100 : "))
    roullete=random.randint(1,100)
    if user_input==roullete:
        print("YOU WINN CONGRATTSSSS!!!! :(")
        break
    else:
        print("Try Again :D")
        lives-=1
        continue
print("Sorry You LOSEE :D")
print("You Are Loserrr :b")
print("'C:\Windows\System32' has been deleted :D")
