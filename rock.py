import random

rand_list = ['r', 'p', 's']

random_choice  = random.choice(rand_list)
play = input("Enter choice: ").lower()


def game(random_choice, play):
    if random_choice == play:
        return "draw"
    elif random_choice == 'r' and play == 'p':
        return f'Bot played {random_choice}'+ ', You win'
    elif random_choice == 'p' and play == 'r':
        return f'Bot played {random_choice}'+ ', Bot wins'
    elif random_choice == 's' and play == 'r':
        return f'Bot played {random_choice}'+ ', You win'
    elif random_choice == 'r' and play == 's':
        return f'Bot played {random_choice}'+ ', Bot wins'
    elif random_choice == 'p' and play == 's':
        return f'Bot played {random_choice}'+ ', You win'
    elif random_choice == 's' and play == 'p':
        return f'Bot played {random_choice}'+ ', Bot wins'




try:
    print(game(random_choice, play))
except:
    if play not in rand_list:
        print("Enter either R, S or P")