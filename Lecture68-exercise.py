import random

win_num = 43
guess = 1
number =int(input("Guess a number between 1 and 100:"))
game_over =False
while not game_over:
    if number<win_num:
        print("too low")
        guess+=1
        number=int(input("Guess  again:"))
    else:
        print("too high")
        guess+=1
        number=int(input("guess again:"))
