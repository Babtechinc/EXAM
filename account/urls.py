from django.urls import path
from account import views

urlpatterns = [
    path('login',views.login_in, name='login'),
]