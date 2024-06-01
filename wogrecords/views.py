from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Level, Record

def index(request):
    levels_list = Level.objects.all()
    records_list = Record.objects.all()
    levels_count = Level.objects.all().count()
    records_count = Record.objects.all().count()

    return render(
        request,
        'index.html',
        context = {'levels_list' : levels_list, 'records_list' : records_list, 'levels_count' : levels_count, 'records_count' : records_count},
    )

def history(request):
    levels_list = Level.objects.all()
    records_list = Record.objects.all()

    record_type = request.GET.get("SelectRecordType")
    if record_type and record_type != "0":
        records_list = records_list.filter(Type = record_type)

    level_select = request.GET.get("SelectRecordLevel")
    if level_select and level_select != "0":
        records_list = records_list.filter(LevelName = level_select)

    return render(
        request,
        'history.html',
        context = {'levels_list' : levels_list, 'records_list' : records_list, 'level_select' : level_select, 'record_type' : record_type},
    )


def index2(request):
    return render(
        request,
        'index2.html',
    )
    
def history2(request):
    return render(
        request,
        'history2.html',
    )