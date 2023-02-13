from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', views.accounts_list, name='list'),
    path('watch/<int:account_id>/', views.watch, name='watch'),
    path('accounts/create', views.AccountCreate.as_view(), name='create'),
    path('accounts/<int:pk>/update/', views.AccountUpdate.as_view(), name='accounts_update'),
    path('accounts/<int:pk>/delete/', views.AccountDelete.as_view(), name='accounts_delete'),
    path('movies/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('accounts/signup/', views.signup, name='signup'),
]