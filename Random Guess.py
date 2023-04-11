import random

Secret_Number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Picker = random.choice(Secret_Number)
Guess_count = 0
Guess_Limit = 3

while Guess_count < Guess_Limit:
    Guess = int(input("Guess: "))
    Guess_count += 1
    if Guess == Picker:
        print("BINGO!!")
        break
else: print("LOSER!!")
