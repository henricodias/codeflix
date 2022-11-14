from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class Homepage(TemplateView):
    template_name = "homepage.html"

class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list -> lista de filmes do modelo

class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # object -> um item do filme


# criar uma view é o mesmo que criar uma página nova
# sempre que for criar uma página nova no site, criar view / url / html (template)

# def homepage(request):
#     return render(request, "homepage.html")

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)

