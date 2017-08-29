from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
    context = {
        # "leagues": League.objects.filter(name__contains="Baseball"),
        # "leagues": League.objects.filter(name__contains="Womens"),
        # "leagues": League.objects.filter(name__contains="Hockey"),
        # "leagues": League.objects.exclude(name__contains="Football"),
        # "leagues": League.objects.filter(name__contains="Conference"),
        "leagues": League.objects.filter(name__contains="Atlantic"),
        # "teams": Team.objects.filter(location__contains="Dallas"),
        # "teams": Team.objects.filter(team_name__contains="Raptors"),
        # "teams": Team.objects.filter(location__contains="City"),
        # "teams": Team.objects.filter(team_name__startswith="T"),
        "teams": Team.objects.all(),
        # "players": Player.objects.filter(last_name__contains="Cooper"),
        # "players": Player.objects.filter(first_name__contains="Joshua"),
        # "players": Player.objects.filter(last_name__contains="Cooper").exclude(first_name__contains="Joshua"),
        "players": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt"),
    }
    return render(request, "leagues/index.html", context)

def make_data(request):
    team_maker.gen_leagues(10)
    team_maker.gen_teams(50)
    team_maker.gen_players(200)

    return redirect("index")