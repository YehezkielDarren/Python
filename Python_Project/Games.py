import random
def RockPapScis():
    print("--ROCK PAPPER SCISSORS GAME--")
    user_Scores=0
    bot_Scores=0
    options=['rock','paper','scissors']
    round=1
    #rock = 0; paper = 1; scissors = 2
    while True:
        print(f"Round {round}.")
        round+=1    
        users_Input=input("Type Rock(R)/Paper(P)/Scissors(S) or Q to quit : ").lower()
        number=random.randint(0,2)
        bot_Input=options[number]
        if users_Input=="q":
            break
        if users_Input not in ["rock",'paper','scissors','r','p','s']:
            continue
        print(f"Computer pick '{bot_Input}'.")
        if users_Input=="r" and bot_Input=="scissors":
            user_Scores+=1
            print("You Win")
        elif users_Input=="r" and bot_Input=="paper":
            bot_Scores+=1
            print("You Lose")
        elif users_Input=="p" and bot_Input=="scissors":
            bot_Scores+=1
            print("You Lose")
        elif users_Input=="p" and bot_Input=="rock":
            user_Scores+=1
            print("You Win")
        elif users_Input=="s" and bot_Input=="paper":
            user_Scores+=1
            print("You Win")
        elif users_Input=="s" and bot_Input=="rock":
            bot_Scores+=1
            print("You Lose")
    win= None
    if user_Scores>bot_Scores:
        win="You Win"
    elif user_Scores<bot_Scores:
        win="You Lose"
    elif user_Scores==bot_Scores:
        win="Duece"
    print(f"Bot Scores : {bot_Scores} || User Scores : {user_Scores}\n'{win}'")        
    print("The Game Stop")

def hangman():
    print("--HANGMAN GAME--")
    lives=10
    #given words
    words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"
                 ]
    while True:
        chosen_word=random.choice(words).lower()
        user_input=None #character that user input each round (only 1 character)
        temp_words=[]
        word_guessed=[] #place the each correct character that user input
        for _ in chosen_word:
            word_guessed.append("_")
            
        while (lives!=0)and("_" in word_guessed):
            print("=========================")
            print(f"You has {lives} HP left")
            displaying_guess="".join(word_guessed)
            print(displaying_guess)
            print("=========================")
            try:
                user_input=input("Type one word 'a-z' or 'esc' to quit : ").lower()
                print("=========================")   
            except:
                print("Invalid Input. Try Again!!")
                continue
            else:
                if  not user_input.isalpha() or len(user_input)!=1:
                    if user_input=="esc":
                        main()
                    print("Invalid Input. Try Again!!")
                    continue
                elif user_input in word_guessed:
                    print(f"This word '{user_input}' has already guessed by user, Try Again !")
                    continue
            if (user_input in chosen_word):
                for i in range(len(chosen_word)):
                    if user_input in chosen_word[i]:
                        word_guessed[i]=user_input
            elif (user_input not in chosen_word):
                if user_input in temp_words:
                    print(f"Wrong Guessed and You Alredady Guess It")
                    lives-=1
                else:
                    temp_words.append(user_input)
                    print(f"Wrong guess !!")
                    lives-=1
                continue
            
        if "_" not in word_guessed:
            print(f"You Win, CONGRATSSS!!!\nLife Remaining : {lives} HP left")
            play_again=input("Do You Want To Play Again ?").lower()
            if play_again not in ("yes","y","true","t"):
                quit()
            else:
                main() 
            
        if ("_" in word_guessed) and lives==0:
            print("You lose !!!")
            print(f"The answer is : '{chosen_word}'.")
            play_again=input("Do You Want To Play Again ?").lower()
            if play_again not in ("yes","y","true","t"):
                quit()
            else:
                main()        
                



def main():
    print("Python Games")
    print("=====================")
    print("Choose :")
    print("1. Rock-Paper-Scissors")
    print("2. Hang Man")
    print("3. Tic Tac Toe 'Still Developed' ")
    print("4. -")
    print("5. -")
    print("=====================")
    options=int(input("Input the number list : "))
    if options==1:
        RockPapScis()
    elif options==2:
        hangman()
    else:
        print("There is no game available or still under developing")

if __name__=='__main__':
    main()