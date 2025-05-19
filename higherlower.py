
from art import logo,vs
from gamedata import data 
import random


def format_data(choice):
    ''''Format the data into printable format'''
    choice_name = choice["name"]
    choice_description=choice["description"]
    choice_country=choice["country"]

    return f"{choice_name}, a {choice_description}, from {choice_country}"

def _check_answer(player_guess,a_follower_count,b_follower_count):
    """Take player guess and return if they are right"""
    if a_follower_count > b_follower_count:
        return player_guess=="a"
    else:
        return  player_guess=="b"
print(logo)
score=0
game_should_continue=True
choice_b=random.choice(data)
while game_should_continue:
    choice_a=choice_b
    choice_b= random.choice(data)
    if choice_a == choice_b:
        choice_b = random.choice(data)

    print(f"Compare A :{format_data(choice_a)}.")
    print(vs)
    print(f"Against B :{format_data(choice_b)}.")

    a_follower_count = choice_a["follower_count"]
    b_follower_count = choice_b["follower_count"]
    player_guess=input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n"*20)

    is_correct=_check_answer(player_guess,a_follower_count,b_follower_count)

    if is_correct:
        score+=1
        print(f"You\'re right! Current score {score} ")
    else:
        print(f"Sorry, that\'s wrong! Final score: {score}")
        game_should_continue = False