from django.shortcuts import redirect, render
from django.utils.functional import SimpleLazyObject
from apptheyrdead.brain import grafico
from site.theyrdead.models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    usuario = request.user.is_authenticated

    luck = ""

    if request.method == 'POST':
        luck = 20 if request.POST.get('luck') == '' else request.POST.get('luck')
        luck = int(luck)
        if request.POST.get('entity') == 'human':
            refreshEntity("human", luck)
        elif request.POST.get('entity') == 'weak':
            refreshEntity("weak", luck)
        elif request.POST.get('entity') == 'strong':
            refreshEntity("strong", luck)
        elif request.POST.get('entity') == 'clear':
            zerar()
    
    entidade = getOrCreateEntity()
    graf = grafico.getGrafico(entidade)
    context = {'user': usuario, 'graf': graf, 'ent':entidade, 'luck': luck}

    return render(request, "index-tad.html", context)

@login_required(login_url='/admin')
def logoutUser(request):
    logout(request)
    return redirect('index-tad')
