import random 

choices = {
    "r":"rock",
    "p":"paper",
    "s":"scissors"
}
computer_choice = random.choice(list(choices.keys()))
user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ")


if user_choice not in choices:
    print("Invalid choice. Please choose r, p, or s.")

else:
    print(f"Computer chose: {choices[computer_choice]}")
    print(f"You chose: {choices[user_choice]}")

    if computer_choice == user_choice:
        print("It's a tie!")

    elif (computer_choice == "r" and user_choice == "s") or (computer_choice == "p" and user_choice == "r") or (computer_choice == "s" and user_choice == "p"):
        print("Computer wins!")
    else:        print("You win!")

