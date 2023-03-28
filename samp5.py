import random

def play():
    user = input("Rock, paper or scissors? ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])
    print("Computer plays", computer)

    if user == computer:
        return "It's a tie!"
    
    if is_win(user, computer):
        return "You win!"
    
    return "You lost!"

def is_win(player, opponent):
    # Return True if player wins
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True

print(play())
