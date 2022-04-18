from django import forms

SEARCH_CHOICES = [
    ('state', 'State'),
    ('city', 'City'),
]

class SearchForm(forms.Form):
    category = forms.ChoiceField(label = 'Search by',choices = SEARCH_CHOICES)
    search_text = forms.CharField(label = 'Search')
    
