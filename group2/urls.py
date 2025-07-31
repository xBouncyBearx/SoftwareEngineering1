from django.urls import path, include
from . import views


app_name = 'group2'
urlpatterns = [
  path("chat/", include('group2_chat.urls')),
  path('api/v1/', include('group2.api.v1.urls')),
  path('', views.home, name='group2'),
  path('complete-profile/', views.complete_profile, name='complete_profile'),
  path('search/', views.search, name='search'),
]
