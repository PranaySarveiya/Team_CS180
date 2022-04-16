from django.urls import path
from . import views


urlpatterns = [
	path('search', views.search, name='search'),
	path('', views.index, name='index'),
	path('search-state', views.AccidentByState, name = 'search-state'),
	path('top-5-states', views.Top5States, name='top-5-states')
]