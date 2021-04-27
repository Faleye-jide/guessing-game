import random

name = "jide"
guess_name = ""
guess_limit = 3
out_of_guess = False
guess_count = 0

while guess_name != name and not (out_of_guess):
    if guess_count < guess_limit:
        guess_name = input("Enter a name: ")
        guess_count +=1
    else:
        out_of_guess = True

if out_of_guess:
    print("you lose")
else:
    print("you win")