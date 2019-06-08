from django.shortcuts import render
from django.http import HttpResponse
from .models import Contest
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
    return HttpResponse("Beermasters contest: %s!!" % contest_id)

