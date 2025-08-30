import random

print("Rules for winning : \n"
      + "Rock Vs Paper --> Paper wins\n"
      + "Rock Vs Scissor --> Rock wins\n"
      + "Paper Vs Scissor --> Scissor wins\n")

while True:

    print("Enter Choice \n  1 - Rock\n  2 - Paper\n  3 - Scissor\n" )
    choice = int(input("Enter your choice :"))

    while choice > 3 or choice < 1:
        print("Please Enter valid choice!")

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"

    print("User choice is : " , choice_name)
    print("Computer's turn ---")

    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"

    print("Computer's choice : " , comp_choice_name)
    print(f"{choice_name} Vs {comp_choice_name}")

    if choice == comp_choice:
        result = "Draw"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = "Paper"                    
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = "Rock"
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = "Scissor"

    if result == "Draw":
        print("<-- TIE -->")
    elif result == choice_name:
        print("User Wins!!!")
    else:
        print("Computer Wins!!!")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == "n":
        break


print("Thans for playing.")