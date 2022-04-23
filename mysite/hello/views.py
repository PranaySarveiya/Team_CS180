from django.shortcuts import render
from django.http import HttpResponse
from hello.csv_read import dataset
from .forms import SearchForm
from .forms import InsertForm
from .forms import DeleteForm
from .forms import UpdateForm
import math
import time
# Create your views here.

statesAbv = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", 
          "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", 
          "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", 
          "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
statesName = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Washington DC", "Delaware", "Florida",
               "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
               "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
               "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
               "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", 'Wyoming']

accidents = dataset()

def welcome(request):
    return render(request, "hello/welcome.html")



def index(request):
    #accidents = dataset()
    row = accidents.getRow()
    return HttpResponse(row.description)

def search(request):
    if request.method == 'POST':
        #get user input
        form = SearchForm(request.POST)
        #check if input is valid
        if form.is_valid():
            #grabs puts the user input into variables
            category = form.cleaned_data['category']
            search_text = form.cleaned_data['search_text']

            #call function to return num of accidents in a state if category is state
            if(category == 'state'):
                return SearchByState(search_text)
            #TODO: implement search for city
            elif(category == 'city'):
                print(category, search_text)

    #if request is not a post, or form input is not valid simply load search.html
    #pass form to the html file
    form = SearchForm()
    return render(request, "hello/search.html", {'form': form})

def SearchByState(search_param):
    if search_param in statesAbv:
        return HttpResponse(AccidentByState(search_param))
    # elif search_param == "Top 5":
    #     return Top5States(request)
    else:
        form = SearchForm()
        print(search_param + " is not a state abbreviation or Top 5")   #for debugging
        return render(request, "hello/search.html", {'form': form})

def SearchState(request):
    if request.method == 'POST':
        state = request.POST['state']
        return HttpResponse(state)
    else:
        return render(request, "hello/state_select.html")

# changed to a helper function for the above search
def AccidentByState(stateAbbreviation): #ToDo: need to integrate with state_select to display # of accidents for selected state
    #accidents = dataset()
    cnt = 0
    for row in accidents.list:
        if row.state == stateAbbreviation:
            #NY = row.street + "\n" #removed for now since we're not using it
            cnt += 1
    stateName = statesName[statesAbv.index(stateAbbreviation)]
    string = stateName + " has " + str(cnt) + " accidents"
    return string

def Top5States(request):
    #accidents = dataset()
    total = len(accidents.list)
    stateCount = [0] * 51
    percent = [0] * 51

    s_time = time.time()
    for row in accidents.list:
        pos = statesAbv.index(row.state)
        stateCount[pos] += 1
    for i in range(len(percent)):
        percent[i] = math.trunc(stateCount[i]/total*10000)/100
        
    print("2nd search-",time.time()-s_time)

    states = zip(statesAbv, stateCount, percent)
    
    states = sorted(states, key=lambda tup: tup[1], reverse = True)[:5]
    # print(total)
    string = ""
    html_string = ""
    
    
    # for i in range(5):
    #     string = states[i][0] + " " + str(states[i][1])
    #     percent.append (math.trunc(states[i][1]/total*10000)/100)
    #     string = "<tr>" + "<td>" + str(i+1) + "</td>" + "<td>" + states[i][0] + "</td>" + "<td>" + str(states[i][1]) + "</td>" + "<td>" + str(percent[i]) + "</td>" + "</tr>" + "\n"
    #     html_string += string
        # print (html_string)
        #html_string = html.unescape(html_string)
        

    #print(states)
    states_name, states_no, percent = zip(*states)
    
    return render(request, 'hello/top_5_states.html', 
                   {'states' : states, 'states_name' : states_name, 'states_no' : states_no ,'percent' : percent ,'html_string' : html_string})

def Modify(request):
    #inserting
    if (request.method == 'POST' and 'insert' in request.POST):
        #get user input
        form = InsertForm(request.POST)
        #check if input is valid
        if form.is_valid():
            #grabs puts the user input into variables
            severity = form.cleaned_data['severity']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            description = form.cleaned_data['description']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            
            #TODO: Somehow insert this information into our file

    #deleting
    elif (request.method == 'POST' and 'delete' in request.POST):
        #get user input
        form = DeleteForm(request.POST)
        #check if input is valid
        if form.is_valid():
            #grabs puts the user input into variables
            selection = form.cleaned_data['selection']
            search_text = form.cleaned_data['search_text']

            #TODO: Somehow delete this information from our file
            #delete all entries with id matching search_text
            if(selection == 'id'):
                print("delete by id")
            #delete all entries with state matching search_text
            elif(selection == 'state'):
                print("delete by state")
            #delete all entries with city matching search_text
            elif(selection == 'city'):
                print("delete by city")
    #updating
    elif (request.method == 'POST' and 'update' in request.POST):
         #get user input
        form = UpdateForm(request.POST)
        #check if input is valid
        if form.is_valid():
            #grabs puts the user input into variables
            id = form.cleaned_data['id']
            updated_field = form.cleaned_data['updated_field']
            new_value = form.cleaned_data['new_value']

            #TODO: implement updating the selected field from the car accident specified by id
            #update severity field with new_value for car with id
            if(updated_field == 'severity'):
                print('update severity field')
            #update start_time field with new_value for car accident with id value
            elif(updated_field == 'start_time'):
                print('update start_time')
            #update end_time field with new_value for car accident with id value
            elif(updated_field == 'end_time'):
                print('update end_time')
            #update description field with new_value for car accident with id value
            elif(updated_field == 'description'):
                print('update description')
            #update street field with new_value for car accident with id value
            elif(updated_field == 'street'):
                print('update street')
            #update city field with new_value for car accident with id value
            elif(updated_field == 'city'):
                print('update city')
            #update state field with new_value for car accident with id value
            elif(updated_field == 'state'):
                print('update state')
            
    #if the backup button is clicked
    elif (request.method == 'POST' and 'backup' in request.POST):
        #TODO: create a backup when this button is clicked
        print("backup")
    #if the import button is clicked
    elif (request.method == 'POST' and 'import' in request.POST):
        #TODO: implement importing stuff
        print('import')
    
    

    #if request is not a post, or form input is not valid simply load modify.html
    #pass form to the html file
    form = InsertForm()
    form2 = DeleteForm()
    form3 = UpdateForm()
    return render(request, "hello/modify.html", {'insert': form, 'delete': form2, 'update': form3})