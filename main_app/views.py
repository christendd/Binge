from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Account, Movie
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')


# @login_required

def accounts_list(request):
    accounts= Account.objects.all()
    return render(request, 'accounts/list.html', {'accounts': accounts})

def watch(request):
    movies = Movie.objects.all()
    return render(request, 'content/movie_list.html', {'movies': movies})

def movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'content/movie_detail.html', {'movie': movie})

class AccountCreate(CreateView):
    model = Account
    fields = ('name',)
    success_url = '/accounts/'
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class AccountUpdate(UpdateView):
    model = Account
    fields = ("name",)

class AccountDelete(DeleteView):
    model = Account
    success_url= '/accounts/'