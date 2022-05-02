from django.urls import path
from . import views


urlpatterns = [
	path('search/', views.search, name='search'),
	path('welcome/', views.welcome, name='welcome'),
	#path('index/', views.index, name='index'),
	#path('search-state/', views.AccidentByState, name = 'search-state'),	#eventually probably want to make this it's own html page
	path('top-5-states/', views.Top5States, name='top-5-states'),
	path('modify/', views.Modify, name='modify')
]