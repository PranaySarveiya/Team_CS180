from django import forms
from hello.models import ImportFile
import os

SEARCH_CHOICES = [
    ('state', 'State'),
    ('city', 'City'),
]

UPDATE_CHOICES = [
    ('severity', 'Severity'),
    ('start_time', 'Start Time'),
    ('end_time', 'End Time'),
    ('description', 'Description'),
    ('street', 'Street'),
    ('city', 'City'),
    ('state', 'State'),
]

DELETE_SELECT_CHOICES = [
    ('id', 'ID Number'),
    ('state', 'State'),
    ('city', 'City'),
]

path = os.path.abspath(os.path.dirname(__file__))
path += "/backupCSV/"

if (not os.path.exists(path)):
    os.makedirs(path)

def updateImport():
    ImportFile.objects.all().delete()

    files = os.listdir(path)
    for backup in files:
	    backup = backup.split(".csv")[0]
	    aFile = ImportFile.objects.create(filename = backup)

class SearchForm(forms.Form):
    category = forms.ChoiceField(label = 'Search by', widget = forms.Select(attrs = {'class' : "form-control"}), choices = SEARCH_CHOICES)
    search_text = forms.CharField(label = 'Search', widget = forms.TextInput(attrs = {'class' : "form-control"}))
    
class InsertForm(forms.Form):
    severity = forms.IntegerField(label = 'Severity:', widget = forms.NumberInput(attrs = {'class' : "form-control"}))
    start_time = forms.CharField(label = 'Start Time:', widget = forms.TextInput(attrs = {'class' : "form-control"}))
    end_time = forms.CharField(label = 'End Time:', widget = forms.TextInput(attrs = {'class' : "form-control"}))
    description = forms.CharField(label = 'Description:', widget = forms.TextInput(attrs = {'class' : "form-control"}))
    street = forms.CharField(label = 'Street:', widget = forms.TextInput(attrs = {'class' : "form-control"}))
    city = forms.CharField(label = 'City:', widget = forms.TextInput(attrs = {'class' : "form-control"}))
    state = forms.CharField(label = 'State:', widget = forms.TextInput(attrs = {'class' : "form-control"}))

class DeleteForm(forms.Form):
    selection = forms.ChoiceField(label = 'Select by', widget = forms.Select(attrs = {'class' : "form-control"}), choices = DELETE_SELECT_CHOICES)
    search_text = forms.CharField(label = 'Search', widget = forms.TextInput(attrs = {'class' : "form-control"}))
    
class UpdateForm(forms.Form):
    id = forms.CharField(label = 'ID', widget = forms.TextInput(attrs = {'class' : "form-control"}))
    updated_field = forms.ChoiceField(label = 'Field to update', widget = forms.Select(attrs = {'class' : "form-control"}), choices = UPDATE_CHOICES)
    new_value = forms.CharField(label = 'New value for field', widget = forms.TextInput(attrs = {'class' : "form-control"}))

class ImportForm(forms.Form):
    updateImport()
    importChoice = forms.ModelChoiceField(label = "Import file", widget = forms.Select(attrs = {'class' : "form-control"}), queryset = ImportFile.objects.all())
