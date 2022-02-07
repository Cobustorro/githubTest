starter = True
while starter:
    import random
    user_input = input("Choose Rock, Paper or Scissors: ")
    choice = ["Rock", "Paper", "Scissors"]
    choice_lower = ["rock", "paper", "scissors"]
    program_choice = random.choice(choice)

    while user_input not in choice or user_input in choice_lower:
        if user_input in choice or user_input in choice_lower:
            break
        else:
            user_input = input("Invalid input! Choose Rock, Paper or Scissors: ")
            continue

    if user_input == program_choice or user_input == program_choice.lower():
        print(f"You chose: {user_input}")
        print(f"It's a draw! The computer chose {program_choice} too!")
    elif user_input == "Rock" or user_input == "rock" and program_choice == "Paper":
        print(f"You chose: {user_input}\nThe program chose: {program_choice}\nThe program won!")
    elif user_input == "Paper" or user_input == "paper" and program_choice == "Rock":
        print(f"You chose: {user_input}\nThe program chose: {program_choice}\nYou won!")
    elif user_input == "Scissors" or user_input == "scissors" and program_choice == "Paper":
        print(f"You chose: {user_input}\nThe program chose: {program_choice}\nYou won!")
    elif user_input == "Rock" or user_input == "rock" and program_choice == "Scissors":
        print(f"You chose: {user_input}\nThe program chose: {program_choice}\nYou won!")
    elif user_input == "Paper" or user_input == "paper" and program_choice == "Scissors":
        print(f"You chose: {user_input}\nThe program chose: {program_choice}\nThe program won!")
    elif user_input == "Scissors" or user_input == "scissors" and program_choice == "Rock":
        print(f"You chose: {user_input}\nThe program chose: {program_choice}\nThe program won!")

    keep_going = input("Do you wanna play again? (Yes/No): ")
    answers = ["Yes", "yes", "No", "no"]
    while keep_going not in answers:
        keep_going = input("Invalid input! Do you wanna play again? (Yes/No): ")
        continue
    if keep_going == "Yes" or keep_going == "yes":
        continue
    else:
        starter = False
