from django import forms

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

class SearchForm(forms.Form):
    category = forms.ChoiceField(label = 'Search by', choices = SEARCH_CHOICES)
    search_text = forms.CharField(label = 'Search')
    
class InsertForm(forms.Form):
    severity = forms.IntegerField()
    start_time = forms.CharField(label = 'Start Time')
    end_time = forms.CharField(label = 'End Time')
    description = forms.CharField(label = 'Description')
    street = forms.CharField(label = 'Street')
    city = forms.CharField(label = 'City')
    state = forms.CharField(label = 'State')

class DeleteForm(forms.Form):
    selection = forms.ChoiceField(label = 'Select by', choices =DELETE_SELECT_CHOICES)
    search_text = forms.CharField(label = 'Search')
    
class UpdateForm(forms.Form):
    id = forms.CharField(label = 'ID')
    updated_field = forms.ChoiceField(label = 'Field to update', choices = UPDATE_CHOICES)
    new_value = forms.CharField(label = 'New value for field')
