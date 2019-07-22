from django.shortcuts import render

# Create your views here.
def index(request): #renderizar uma página // cada aplicação tem um lion 
    return render(request, 'index.html') #busca automaticamente no diretório template