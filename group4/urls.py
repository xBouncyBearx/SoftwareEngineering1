from django.urls import path
from . import views

app_name = 'group4'
urlpatterns = [
  path('', views.home, name='group4')

] 