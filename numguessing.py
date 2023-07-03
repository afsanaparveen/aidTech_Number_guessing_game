import random
number=random.randint(1,100)
name=input("Enter your name")
rules="1.choose number between 1-100 \n 2.If the guessed number is to low we say you to guess high\n 3.If the guessed number is to high we say you to guess low"
message="Hello {} Welcome to number guessing game let me explain the rules of game \n{}"
print(message.format(name,rules))
guess=0
while guess<=10:
    guessnum=int(input("enter the guess number"))
    if guessnum<number:
        print("YOUR guess is too low please guess more than this number")
    elif guessnum>number:
        print("YOUR guess is too high please guess less than this number")
    else:
        print("YOU WON THE GAME CONGRATS")

    guess=guess+1
print("GAME OVER")
print("YOU REACHED YOUR GUESS LIMIT THANKS FOR PLAYING ")
print("if you want to play again enter PLAYAGAIN else write QUIT THE GAME")
again=input("enter you wishing")
if again=="playagain":
    guess=0
    while guess<=10:
        guessnum=int(input("enter the guess number"))
        if guessnum<number:
            print("YOUR guess is too low please guess more than this number")
        elif guessnum>number:
            print("YOUR guess is too high please guess less than this number")
        else:
            print("YOU WON THE GAME CONGRATS")
        guess=guess+1
        print("try again later")        
else:
    print("quit the game")