from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Account, Movie
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required
def accounts_list(request):
    accounts= Account.objects.filter(user=request.user)
    return render(request, 'accounts/list.html', {'accounts': accounts})

@login_required
def watch(request, account_id):
    account = Account.objects.get(id=account_id)
    movies = Movie.objects.all()
    return render(request, 'content/movie_list.html', {'movies': movies})

@login_required
def movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'content/movie_detail.html', {'movie': movie})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('list')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class AccountCreate(LoginRequiredMixin, CreateView):
    model = Account
    fields = ('name',)
    success_url = '/accounts/'
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class AccountUpdate(LoginRequiredMixin, UpdateView):
    model = Account
    fields = ("name",)

class AccountDelete(LoginRequiredMixin, DeleteView):
    model = Account
    success_url= '/accounts/'