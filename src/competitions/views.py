from django.shortcuts import render
from django.http import HttpResponse
from .models import (Contest, ContestParticipant, ContestTable, 
	ContestTableItem, Item)
from django.template import loader

# Create your views here.
def index(request):
    latest_contest_list = Contest.objects.order_by('start_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_contest_list': latest_contest_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, contest_id):
    contest = Contest.objects.get(pk=contest_id)
    cps = ContestParticipant.objects.filter(contest=contest_id).filter(user=request.user)
    cpts = ContestTable.objects.filter(contest=contest_id)
    return render(request, 'contest_detail.html', 
            {'contest': contest, 'participant': cps[0], 'tables': cpts})

def scoresheet(request, table_id, item_id):
    table = ContestTable.objects.get(pk=table_id)
    item = Item.objects.get(pk=item_id)
    cps = ContestParticipant.objects.filter(contest=table.contest.id).filter(user=request.user)
    contest = Contest.objects.get(pk=table.contest.id)
    return render(request, 'score_sheet.html', {'participant': cps[0], 'contest': contest,
	'table': table, 'contest': contest, 'item': item})

def score(request, contest_id):
    contest = Contest.objects.get(pk=contest_id)
    return HttpResponse("Scoring beer %s category %s contest %s" % (1, 1, contest.id))

def table(request, table_id):
    table = ContestTable.objects.get(pk=table_id)
    items = ContestTableItem.objects.filter(table=table_id)
    cps = ContestParticipant.objects.filter(contest=table.contest.id).filter(user=request.user)
    return render(request, 'table_detail.html', {'user': request.user,
	'items': items, 'table': table, 'participant': cps[0]})

