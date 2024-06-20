import random

def get_choices():
    Player_choice = input("Please enter a choice \"rock\", \"paper\" or \"scissors\" : ")
    choice_list = ["rock", "paper", "scissors"]
    Computer_choice = random.choice(choice_list)
    choice = {"Player" : Player_choice, "Computer" : Computer_choice}
    return choice
def check_win(Player, Computer):
    print(f"You choise {Player}, and the computer choise {Computer}")
    if Player == Computer:
        return "Its a draw"
    elif Player == "rock":
        if Computer == "paper":
            return "You lose"
        else:
            return "You win"
    elif Player == "paper":
        if Computer == "rock":
            return "You win"
        else:
            return "You lose"
    elif Player == "scissors":
        if Computer == "rock":
            return "You win"
        else:
            return "You lose"
    else:
        return "Error, please enter a valide option"
    
chioce = get_choices()
result = check_win(chioce["Player"], chioce["Computer"])
print(result)
