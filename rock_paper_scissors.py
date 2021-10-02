import random


def play():
    pick = input("'r' for rock, 'p' for paper 's' for scissors: ")
    cpu = random.choice(['r', 's', 'p'])
    abbreviation = {'r': 'rock',
                    's': 'scissors',
                    'p': 'paper'}

    def winner(user, computer):
        if (pick == 'r' and cpu == 's') or (pick == 's' and cpu == 'p') or (pick == 'p' and cpu == 'r'):
            print(f"Winner is {abbreviation[user]} because {abbreviation[user]} beats {abbreviation[computer]}")
        elif pick == cpu:
            print("draw")
        else:
            print(f"You lost winner is {abbreviation[computer]}")

    winner(pick, cpu)


play()
