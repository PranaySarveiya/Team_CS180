from django.shortcuts import render
from django.http import HttpResponse
from hello.csv_read import dataset
import math
# Create your views here.

statesAbv = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", 
          "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", 
          "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", 
          "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def welcome(request):
    return render(request, "hello/search.html")



def index(request):
    example = dataset()
    row = example.getRow()
    return HttpResponse(row.description)

def search(request):
    if request.method == 'POST':
        search_param = request.POST["textfield"]
        if search_param in statesAbv:
            return HttpResponse(AccidentByState(search_param))
        elif search_param == "Top 5":
            return Top5States(request)
        else:
            print(search_param + " is not a state abbreviation or Top 5")   #for debugging
            return render(request, "hello/search.html")
    else:
        return render(request, "hello/search.html")

def SearchState(request):
    if request.method == 'POST':
        state = request.POST['state']
        return HttpResponse(state)
    else:
        return render(request, "hello/state_select.html")

# changed to a helper function for the above search
def AccidentByState(stateAbbreviation): #ToDo: need to integrate with state_select to display # of accidents for selected state
    accidents = dataset()
    cnt = 0
    for row in accidents.list:
        if row.state == stateAbbreviation:
            #NY = row.street + "\n"
            cnt += 1
            
    string = stateAbbreviation + " has " + str(cnt) + " accidents"
    return string

def Top5States(request):
    accidents = dataset()
    total = len(accidents.list)
    stateCount = []
    percent = []
    for i in statesAbv:
        cnt = 0
        for row in accidents.list:
            if i == row.state:
                cnt += 1
        stateCount.append(cnt)
        percent.append(math.trunc(cnt/total*10000)/100)
    
    states = zip(statesAbv, stateCount, percent)
    
    states = sorted(states, key=lambda tup: tup[1], reverse = True)[:5]
    # print(total)
    string = ""
    html_string = ""
    
    
    for i in range(5):
        string = states[i][0] + " " + str(states[i][1])
        percent.append (math.trunc(states[i][1]/total*10000)/100)
        string = "<tr>" + "<td>" + str(i+1) + "</td>" + "<td>" + states[i][0] + "</td>" + "<td>" + str(states[i][1]) + "</td>" + "<td>" + str(percent[i]) + "</td>" + "</tr>" + "\n"
        html_string += string
        # print (html_string)
        #html_string = html.unescape(html_string)
        

    #print(states)
    states_name, states_no, percent = zip(*states)
    
    return render(request, 'hello/top_5_states.html', 
                   {'states' : states, 'states_name' : states_name, 'states_no' : states_no ,'percent' : percent ,'html_string' : html_string})