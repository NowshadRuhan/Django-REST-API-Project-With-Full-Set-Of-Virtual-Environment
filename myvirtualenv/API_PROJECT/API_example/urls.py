from django.conf.urls import url
from django.urls import path
from API_example import views

app_name = 'api'
urlpatterns = [
    path('', views.IndexView, name='home'),

]
