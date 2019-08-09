# Protocol
from django.http import HttpResponse
from django.shortcuts import redirect
# Templates
from django.shortcuts import render
from django.template import loader
# Validators
from django.core.validators import validate_email
# Exceptions
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
# Models
from django.contrib.auth.models import User
from .models import (Contest, ContestParticipant, ContestTable, 
    ContestTableItem, Item, ContestScoreSheet, Aroma, Apperance,
    Flavor, Mouthfeel)
# General
from django.contrib import messages


def index(request):
    latest_contest_list = Contest.objects.order_by('start_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_contest_list': latest_contest_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, contest_id):
    cps = [request.user]
    participant = None
    contest = Contest.objects.get(pk=contest_id)
    if request.user.id != None:
        cps = ContestParticipant.objects.filter(
        contest=contest_id).filter(user=request.user)
    cpts = ContestTable.objects.filter(contest=contest_id)
    if cps:
        participant = cps[0]
    return render(request, 'contest_detail.html', 
        {'contest': contest, 'participant': participant, 'tables': cpts})

def scoresheet(request, table_id, item_id):
    cps = [request.user]
    table = ContestTable.objects.get(pk=table_id)
    if request.user.id != None:
        cps = ContestParticipant.objects.filter(
        contest=table.contest.id).filter(user=request.user)
    #if not cps:
    #    return render(request, 'score_sheet.html', {})
    table_item = ContestTableItem.objects.get(pk=item_id)
    contest = Contest.objects.get(pk=table.contest.id)
    ss = ContestScoreSheet.objects.filter(table_item=item_id)
    content = {'participant': cps[0], 'contest': contest,
        'table': table, 'contest': contest, 'table_item': table_item}
    if ss:
        content.update({'aroma': ss[0].aroma, 'apperance': ss[0].apperance,
          'flavor': ss[0].flavor, 'mouthfeel': ss[0].mouthfeel,
          'score_sheet': ss[0]})
    return render(request, 'score_sheet.html', content)

def score(request, table_item_id):
    cps = [request.user]
    table_item = ContestTableItem.objects.get(pk=table_item_id)
    table = ContestTable.objects.get(pk=table_item.table.id)
    contest = Contest.objects.get(pk=request.POST['contest_id'])
    for key, value in request.POST.items():
        print("KEY: %s, VALUE: %s" % (key, value))

    p = request.POST
    score = (int(p['aroma_score']) + int(p['apperance_score']) +
        int(p['flavor_score']) + int(p['mouthfeel_score']) +
        int(p['overall_score']))

    if request.user.id != None:
        cps = ContestParticipant.objects.filter(
        contest=table.contest.id).filter(user=request.user)

    content = {'participant': cps[0], 'contest': contest,
    'table': table, 'contest': contest, 'table_item': table_item, 'score': score}
    content.update(p.dict())
    aroma = Aroma(score=p['aroma_score'], malt=p['aroma_malt'], hop=p['aroma_hop'],
        fermentation=p['aroma_fermentation'], other=p['aroma_other'], 
        comment=p['aroma_comment'])

    apperance = Apperance(score=p['apperance_color'], color=p['apperance_color'], 
        transp=p['apperance_transp'], other=p['apperance_other'], 
        comment=p['apperance_comment'])

    flavor = Flavor(score=p['flavor_score'], malt=p['flavor_malt'], 
        hop=p['flavor_hop'], bitterness=p['flavor_bitterness'], 
        fermentation=p['flavor_fermentation'], balance=p['flavor_balance'], 
        final=p['flavor_final'], other=p['flavor_other'], 
        comment=p['flavor_comment'])

    mouthfeel = Mouthfeel(score=p['mouthfeel_score'], body=p['mouthfeel_body'], 
        carbonation=p['mouthfeel_carbonation'], warmth=p['mouthfeel_warmth'], 
        creaminess=p['mouthfeel_creaminess'], astringency=p['mouthfeel_astringency'], 
        other=p['mouthfeel_other'], comment=p['mouthfeel_comment'])

    bi = True if p['bottle_insp'] == 'on' else False

    aroma.save()
    apperance.save()
    flavor.save()
    mouthfeel.save()
    sc = ContestScoreSheet(table_item=table_item, aroma=aroma, apperance=apperance,
        flavor=flavor, mouthfeel=mouthfeel, bottle_insp=bi,
        special_ingredients=p['special_ingredients'], 
        bottle_insp_comment=p['bottle_insp_comment'], 
        overall_score=p['overall_score'], overall_comment=p['overall_comment'], 
        style=p['style'], technical=p['technical'], intangible=p['intangible'], 
        total_score=score)

    sc.save()

    return render(request, 'score_sheet.html', content)

def table(request, table_id):
    cps = [request.user]
    table = ContestTable.objects.get(pk=table_id)
    if request.user.id != None:
        cps = ContestParticipant.objects.filter(
        contest=table.contest.id).filter(user=request.user)
    items = ContestTableItem.objects.filter(table=table_id)
    # TODO: refactor item label to contest_table_item to avoid confusion
    return render(request, 'table_detail.html', {'user': request.user,
    'items': items, 'table': table, 'participant': cps[0]})

    
def register(request):
    if request.method != "POST":
        return render(request, 'register.html')
    else:
        return validate_and_create(request)

def validate_and_create(request):
    p = request.POST

    try:
        validate_email(p['email'])
    except ValidationError:
        messages.warning(request, "Invalid Email")

    if p['password1'] != p['password2']:
        messages.warning(request, "Passwords don't match")

    # Show return if this errors exist
    if len(list(messages.get_messages(request))) > 0:
        return render(request, 'register.html')

    try:
        user = User.objects.create_user(username = p['username'],
            email = p['email'],
            password = p['password1'])
        messages.success(request, "Congratulations you're now part of the BeerMasters community")
        return redirect("/accounts/login")
    except IntegrityError:
        messages.warning(request, "Username already exists")
        return render(request, 'register.html')
    except Exception as e:
        messages.error(request, "Error: %s" % e)
        return render(request, 'register.html')

    messages.info(request, "Redirected from register")
    return redirect("/")

def profile(request):
    return render(request, 'user_profile.html')

