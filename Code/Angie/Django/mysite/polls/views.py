from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, 'polls/index.html')

    # game_record = GameRecord(winner='nobody')
    # game_record.save()
    #
    # return HttpResponse('game record successfully saved')