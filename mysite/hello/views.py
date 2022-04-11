from django.shortcuts import render
from django.http import HttpResponse
from hello.csv_read import dataset
# Create your views here.

def index(request):
	example = dataset()
	row = example.getRow()
	return HttpResponse(row.description);
