from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Level, Record, Record2, Player

def index(request):
    levels_list = Level.objects.all()
    records_list = Record.objects.all()
    levels_count = Level.objects.all().count()
    records_count = Record.objects.all().count()

    return render(
        request,
        'index.html',
        context = {'levels_list' : levels_list, 'records_list' : records_list, 'levels_count' : levels_count, 'records_count' : records_count, 'versions_list' : ["1.3","1.5"] },
    )

def history(request):
    record_type = request.GET.get("SelectRecordType")
    level_select = request.GET.get("SelectRecordLevel")
    levels_list = Level.objects.all()
    records_list = []

    if (not record_type) or (not level_select) or record_type == "0" or level_select == "0":
        records_list = []
    else:
        records_list = Record.objects.all()

        if record_type and record_type != "0" and record_type != "1":
            records_list = records_list.filter(Type = record_type)

        if level_select and level_select != "0" and level_select != "1":
            records_list = records_list.filter(LevelName = level_select)

    return render(
        request,
        'history.html',
        context = {'levels_list' : levels_list, 'records_list' : records_list, 'level_select' : level_select, 'record_type' : record_type},
    )

def leaderboards(request):
    players_list = Player.objects.all()
    players_count = Player.objects.all().count()

    player_current_record_dict = {}
    player_history_record_dict = {}
    for player in players_list:
        player_current_record_dict[player.Name] = {"B" : 0, "M" : 0, "T" : 0, "O" : 0, "SUM" : 0}
        player_history_record_dict[player.Name] = {"B" : 0, "M" : 0, "T" : 0, "O" : 0, "SUM" : 0}
    for record in Record.objects.all():
        if record.Player:
            player_history_record_dict[record.Player.Name][record.Type] += 1
            player_history_record_dict[record.Player.Name]["SUM"] += 1
    for level in Level.objects.all():
        records_list = []
        if level.BallRec:
            records_list.append(level.BallRec)
        if level.MoveRec:
            records_list.append(level.MoveRec)
        if level.TimeRec:
            records_list.append(level.TimeRec)
        if level.OCDTimeRec:
            if level.TimeRec and level.TimeRec != level.OCDTimeRec:
                records_list.append(level.OCDTimeRec)
        for record in records_list:
            if record.Player:
                player_current_record_dict[record.Player.Name][record.Type] += 1
                player_current_record_dict[record.Player.Name]["SUM"] += 1

    # print(player_history_record_dict)
    # print(type(player_history_record_dict))
    # print(player_current_record_dict)

    player_history_record_list = []
    player_current_record_list = []
    for key in player_history_record_dict:
        val = player_history_record_dict[key]
        player_history_record_list.append([key,val["B"],val["M"],val["T"],val["O"],val["SUM"]])
    for key in player_current_record_dict:
        val = player_current_record_dict[key]
        player_current_record_list.append([key,val["B"],val["M"],val["T"],val["O"],val["SUM"]])

    player_history_record_list.sort(reverse = True, key = lambda item: item[5])
    player_current_record_list.sort(reverse = True, key = lambda item: item[5])

    while(len(player_history_record_list) > 0 and player_history_record_list[-1][5] == 0):
        player_history_record_list.pop()
    while(len(player_current_record_list) > 0 and player_current_record_list[-1][5] == 0):
        player_current_record_list.pop()
        
    # print(player_history_record_list)
    # print(player_current_record_list)

    player_ball_list = list(players_list)
    for player in player_ball_list:
        if not player.Balls:
            player.Balls = 0
    player_ball_list.sort(reverse = True, key = lambda item: item.Balls)
    player_move_list = list(players_list)
    for player in player_move_list:
        if not player.Moves:
            player.Moves = 9999
    player_move_list.sort(reverse = False, key = lambda item: item.Moves)
    player_time_list = list(players_list)
    for player in player_time_list:
        if not player.Time:
            player.Time = 99999000
    player_time_list.sort(reverse = False, key = lambda item: item.Time)

    return render(
        request,
        'leaderboards.html',
        context = {'players_list' : players_list, 
                   'players_count' : players_count, 
                   'player_history_record_list' : player_history_record_list, 
                   'player_current_record_list' : player_current_record_list,
                   'player_ball_list' : player_ball_list[0:10],
                   'player_move_list' : player_move_list[0:10],
                   'player_time_list' : player_time_list[0:10],
                   },
    )

def index2(request):
    levels_list = Level.objects.all()
    records_list = Record2.objects.all()
    levels_count = Level.objects.all().count()
    records_count = Record2.objects.all().count()

    return render(
        request,
        'index2.html',
        context = {'levels_list' : levels_list, 'records_list' : records_list, 'levels_count' : levels_count, 'records_count' : records_count },
    )
    
def history2(request):
    record_type = request.GET.get("SelectRecordType")
    level_select = request.GET.get("SelectRecordLevel")
    levels_list = Level.objects.all()
    records_list = []

    if (not record_type) or (not level_select) or record_type == "0" or level_select == "0":
        records_list = []
    else:
        records_list = Record2.objects.all()

        if record_type and record_type != "0" and record_type != "1":
            records_list = records_list.filter(Type = record_type)

        if level_select and level_select != "0" and level_select != "1":
            records_list = records_list.filter(LevelName = level_select)

    return render(
        request,
        'history2.html',
        context = {'levels_list' : levels_list, 'records_list' : records_list, 'level_select' : level_select, 'record_type' : record_type},
    )