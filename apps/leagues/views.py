from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
    context = {

        # Simple finds

        # "leagues": League.objects.filter(name__contains="Baseball"),
        # "leagues": League.objects.filter(name__contains="Womens"),
        # "leagues": League.objects.filter(name__contains="Hockey"),
        # "leagues": League.objects.exclude(name__contains="Football"),
        # "leagues": League.objects.filter(name__contains="Conference"),
        # "leagues": League.objects.filter(name__contains="Atlantic"),
        # "teams": Team.objects.filter(location__contains="Dallas"),
        # "teams": Team.objects.filter(team_name__contains="Raptors"),
        # "teams": Team.objects.filter(location__contains="City"),
        # "teams": Team.objects.filter(team_name__startswith="T"),
        # "teams": Team.objects.all(),
        # "players": Player.objects.filter(last_name__contains="Cooper"),
        # "players": Player.objects.filter(first_name__contains="Joshua"),
        # "players": Player.objects.filter(last_name__contains="Cooper").exclude(first_name__contains="Joshua"),
        # "players": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt"),

        # Foreign key
        
        # "leagues": League.objects.all(),
        # "teams": Team.objects.filter(league = League.objects.filter(name = "Atlantic Soccer Conference")),
        # "teams": Team.objects.all(),
        # "players": Player.objects.filter(curr_team = Team.objects.filter(team_name = "Penguins", location = "Boston")),
        # "players": Player.objects.filter(curr_team__league__name = "International Collegiate Baseball Conference"),
        # "players": Player.objects.filter(curr_team__league__name = "American Conference of Amateur Football", last_name = "Lopez"),
        # "players": Player.objects.filter(curr_team__league__sport = "Football"),
        # "players": Player.objects.all()
        # "players": Player.objects.filter(last_name__contains="Flores").exclude(curr_team__team_name="Roughriders",curr_team__location="Washington"),
        # "teams": Team.objects.filter(curr_players__first_name = "Sophia"),
        # "leagues": League.objects.filter(teams__curr_players__first_name = "Sophia"),

        # ManyToMany Relationships

        # "teams": Team.objects.filter(all_players__first_name = "Samuel", all_players__last_name = "Evans"),
        # "teams": Team.objects.filter(all_players__first_name = "Jacob", all_players__last_name = "Gray").exclude(team_name = "Colts", location = "Oregon"),
        "teams": Team.objects.annotate(x = Count('all_players')).filter(x__gt=11),
        # "players": Player.objects.filter(all_teams__team_name = "Tiger-Cats", all_teams__location = "Manitoba")
        # "players": Player.objects.filter(all_teams__team_name = "Vikings", all_teams__location = "Wichita").exclude(curr_team__team_name = "Vikings", curr_team__location = "Wichita")
        # "players": Player.objects.filter(first_name = "Joshua", all_teams__league__name = "Atlantic Federation of Amateur Baseball Players")
        "players": Player.objects.annotate(x = Count('all_teams')).order_by('-x')
        # "players": Player.objects.all()

    }
    return render(request, "leagues/index.html", context)

def make_data(request):
    team_maker.gen_leagues(10)
    team_maker.gen_teams(50)
    team_maker.gen_players(200)

    return redirect("index")