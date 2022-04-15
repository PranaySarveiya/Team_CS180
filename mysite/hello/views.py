from django.shortcuts import render
from django.http import HttpResponse
from hello.csv_read import dataset
# Create your views here.

def welcome(request):
	return render(request, "hello/search.html")



def index(request):
	example = dataset()
	row = example.getRow()
	return HttpResponse(row.description)

def search(request):
	if request.method == 'POST':
		search_param = request.POST["textfield"]
		return HttpResponse(search_param)
	else:
		return render(request, "hello/search.html")



