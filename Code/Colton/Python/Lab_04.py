import random
magic_answers = ['Yes', 'No', 'Maybe', 'Does not look good', 'Ask me later', 'Things are looking up', 'outlook good', 'reply hazy try again']
while True:
    input(f"Hello, I am the magic eight ball ask me a question!>")
    print(f"{random.choice(magic_answers)}.")
    end_game = input(f"Roll again? Yes or No?")
    if end_game == 'no':
        break