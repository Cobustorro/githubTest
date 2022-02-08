starter = True
while starter:
    import random
    user_input = input("Choose Rock, Paper or Scissors: ")
    choice = ["rock", "paper", "scissors"]
    program_choice = random.choice(choice)

    while user_input.lower() not in choice:
        if user_input.lower() in choice:
            break
        else:
            user_input = input("Invalid input! Choose Rock, Paper or Scissors: ")
            continue

    if user_input.lower() == program_choice:
        print(f"You chose: {user_input.lower()}")
        print(f"It's a draw! The computer chose {program_choice.lower()} too!")
    elif user_input.lower() == "rock" and program_choice == "paper":
        print(f"You chose: {user_input.lower()}\nThe program chose: {program_choice.lower()}. The program won!")
    elif user_input.lower() == "paper" and program_choice == "rock":
        print(f"You chose: {user_input.lower()}\nThe program chose: {program_choice.lower()}. You won!")
    elif user_input.lower() == "scissors" and program_choice == "paper":
        print(f"You chose: {user_input.lower()}\nThe program chose: {program_choice.lower()}. You won!")
    elif user_input.lower() == "rock" and program_choice == "scissors":
        print(f"You chose: {user_input.lower()}\nThe program chose: {program_choice.lower()}. You won!")
    elif user_input.lower() == "paper" and program_choice == "scissors":
        print(f"You chose: {user_input.lower()}\nThe program chose: {program_choice.lower()}. The program won!")
    elif user_input.lower() == "scissors" and program_choice == "rock":
        print(f"You chose: {user_input.lower()}\nThe program chose: {program_choice.lower()}. The program won!")

    keep_going = input("Do you wanna play again? (Yes/No): ")
    answers = ["yes", "no"]
    while keep_going.lower() not in answers:
        keep_going = input("Invalid input! Do you wanna play again? (Yes/No): ")
        continue
    if keep_going.lower() == "yes":
        continue
    else:
        starter = False
