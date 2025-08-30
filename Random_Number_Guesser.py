import random

total_guess = 7
my_guesses = 0
a=int(input("Enter starting number : "))
b=int(input("Enter ending number : "))

random_integer = random.randint(a , b)

while my_guesses<total_guess:
    guess = int(input("Enter Guess : "))
    my_guesses+=1

    if guess==random_integer:
        print("Your guess is correct , the number is " , random_integer)
        break
    elif guess<random_integer:
        print("You guessed lower.")
    elif guess>random_integer:
        print("You guessed higher.")          

if my_guesses==total_guess:
    print("Sorry, you've used all your guesses.")