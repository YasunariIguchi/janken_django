import random
from django.shortcuts import render
from .models import GameResult

def janken(request):
    if request.method == "POST":
        user_choice = request.POST.get("choice")
        computer_choice = random.choice(["G", "C", "P"])
        result = determine_winner(user_choice, computer_choice)
        GameResult.objects.create(user_choice=user_choice, computer_choice=computer_choice, result=result)
        return render(request, "result.html", {"result": result, "user_choice": user_choice, "computer_choice": computer_choice})
    return render(request, "play.html")

def determine_winner(user, computer):
    if user == computer:
        return "引き分け"
    elif (user == "G" and computer == "C") or (user == "C" and computer == "P") or (user == "P" and computer == "G"):
        return "勝ち"
    else:
        return "負け"