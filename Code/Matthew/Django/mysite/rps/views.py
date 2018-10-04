from django.shortcuts import render
from django.http import HttpResponse

import random
from .models import GameRecord

def index(request):

    rps = ['rock', 'paper', 'scissors']

    if request.method == 'POST':
        human_choice = request.POST['human_choice']
        computer_choice = random.choice(rps)

        winner = 'nobody'
        if human_choice == computer_choice:
            winner = 'tie'
        elif human_choice == 'rock':
            if computer_choice == 'scissors':
                winner = 'human'
            else:
                winner = 'computer'
        elif human_choice == 'paper':
            if computer_choice == 'rock':
                winner = 'human'
            else:
                winner = 'computer'
        elif human_choice == 'scissors':
            if computer_choice == 'paper':
                winner = 'human'
            else:
                winner = 'computer'

        game_record = GameRecord(winner=winner)
        game_record.save()

        return render(request, 'rps/rps.html', {'rps': rps, 'message': winner + '!!!!!'})

    return render(request, 'rps/rps.html', {'rps': rps})






