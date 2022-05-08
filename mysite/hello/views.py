from re import A
from django.shortcuts import render
from django.http import HttpResponse
from hello.csv_read import dataset
from .forms import SearchForm, InsertForm, DeleteForm, UpdateForm, ImportForm, updateImport
from hello.scatter_plot import update_scatter_plot
import math
import time
import os
import logging
# Create your views here.

#Global Variables:
STATES_ABV = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", 
          "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", 
          "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", 
          "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
STATE_NAMES = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Washington DC", "Delaware", "Florida",
               "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
               "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
               "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
               "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", 'Wyoming']

# US_Accidents_Dec21_updated
#US_Accidents_60000_rows
FILENAME = "US_Accidents_60000_rows"
currentBackup = ""
accidents = dataset(FILENAME)

def welcome(request):
    """
    The first page you see when you enter the website
    """
    return render(request, "hello/welcome.html")

def crashes_by_month(request):
    """
    The analytics page
    """
    return render(request, "hello/crashes_by_month.html")


def search(request):
    """
    The main search function. Options to search by state or city, returns # of accidents.

    Returns:
    render: render of page for SearchByState, SearchByCity, or the main SearchForm if input invalid
    """
    try:
        if request.method == 'POST':
            #get user input
            #return HttpResponse("Hello")
            form = SearchForm(request.POST)
            #check if input is valid
            if form.is_valid():
                #grabs puts the user input into variables
                category = form.cleaned_data['category']
                search_text = form.cleaned_data['search_text']

                #call function to return num of accidents in a state if category is state
                if(category == 'state'):
                    if search_text in STATES_ABV:
                        return SearchByState(request, search_text)
                    else:
                        form = SearchForm()
                        logging.warning(search_text + " is not a state abbreviation or Top 5")   #for debugging
                        return render(request, "hello/search.html", {'form': form})
                elif(category == 'city'):
                    logging.info(category, search_text)
                    return SearchByCity(request, search_text)
    except Exception as e:
        logging.error(e)
    form = SearchForm()
    return render(request, "hello/search.html", {'form': form})

def SearchByState(request, state_abbreviation):
    """
    Search by state used by search function

    Parameters:
    search_param (string): the state name inputted by the user

    Returns:
    return_message_to_user (string): the message to show to user, or in case of error, the search form
    """
    try:
        cnt = 0
        for row in accidents.list:
            if row.state == state_abbreviation:
                cnt += 1
        state_name = STATE_NAMES[STATES_ABV.index(state_abbreviation)]
        return_message_to_user = state_name + " has " + str(cnt) + " accidents"
        return HttpResponse(return_message_to_user)
    except Exception as e:
        logging.error(e)
    form = SearchForm()
    return render(request, "hello/search.html", {'form': form})

def SearchByCity(request, search_param):
    """
    Search by city used by search function

    Parameters:
    search_param (string): the city name inputted by the user

    Returns:
    HttpResponse: the # of accidents, or in case of error, the search form
    """
    try:
        cnt = 0
        for row in accidents.list:
            if row.city == search_param:
                cnt += 1
        message = "City " + search_param + " has " + str(cnt) + " accidents"
        return HttpResponse(message)
    except Exception as e:
        logging.error(e)
    form = SearchForm()
    return render(request, "hello/search.html", {'form': form})

def Top5States(request):
    """
    User presses a button, the top 5 states with the most accidents is outputted in a table

    Returns:
    top_5_states.html (render): rendering of the table
    """
    try:
        total = len(accidents.list)
        logging.info("total entries:", total)
        stateCount = [0] * 51
        percent = [0] * 51

        s_time = time.time()
        for row in accidents.list:
            pos = STATES_ABV.index(row.state)
            stateCount[pos] += 1
        for i in range(len(percent)):
            if(total != 0): #if given an empty csv file
                percent[i] = math.trunc(stateCount[i]/total*10000)/100
            
        logging.info("2nd search-",time.time()-s_time)

        states = zip(STATES_ABV, stateCount, percent)
        
        states = sorted(states, key=lambda tup: tup[1], reverse = True)[:5]
        logging.info(total)
        string = ""
        html_string = ""
            

        logging.info(states)
        states_name, states_no, percent = zip(*states)
        
        return render(request, 'hello/top_5_states.html', 
                    {'states' : states, 'states_name' : states_name, 'states_no' : states_no ,'percent' : percent ,'html_string' : html_string})
    except Exception as e:
        logging.error(e)
    form = SearchForm()
    return render(request, "hello/search.html", {'form': form})

def DeleteRow(column, value):
    """
    Functionality to delete a given row, or delete all rows with a certain city or state

    Parameters:
    column (int): 0, 13, or 15. 0 means delete by id, 13 is delete by state, 15 is delete by value
    value (string): id, state name, or city name
    """
    try:
        # Delete the given rows
        count = accidents.removeRow(column, value)

        # Now write the changed dataset to the base file
        path = os.path.abspath(os.path.dirname(__file__))
        strList = accidents.toList()

        with open(path + "/" + FILENAME + ".csv", "w+") as baseFile:
            for row in strList:
                baseFile.write(str(row))

            baseFile.close()

        logging.info("Deleted " + str(count) + " rows")
        logging.info("Done Reading csv file for delete method")

    except Exception as e:
        logging.error("Something went wrong when deleting")
        logging.error(e)

def InsertRow(insert_row):
    """
    Functionality to insert a single row with some values

    Parameters:
    insert_row (list): list vlaue with a number of values to insert, including id
    """
    try:
        csv_row = [""] * 47
        csv_row[0] = insert_row[0] #ID
        csv_row[1] = insert_row[1] #severity
        csv_row[2] = insert_row[2] #start_time
        csv_row[3] = insert_row[3] #end_time
        csv_row[9] = insert_row[4] #description
        csv_row[11] = insert_row[5] #street
        csv_row[13] = insert_row[6] #city
        csv_row[15] = insert_row[7] #state
        
        path = os.path.abspath(os.path.dirname(__file__))
        with open(path + "/" + FILENAME + ".csv", "a") as dataWrite: # used the file created by csv_trim.py to test
            csv_string = ",".join(csv_row)
            dataWrite.write(csv_string + "\n") # write to file

            accidents.addRow(csv_string.split(",")) #add to data structure

            dataWrite.close()

    except Exception as e:
        logging.error("Something went wrong when inserting")
        logging.error(e)

def Backup():
    """
    Takes the current data and backs it up into a new csv file. Can be brought back with import
    """
    try:
        path = os.path.abspath(os.path.dirname(__file__))
        strList = accidents.toList()

        with open(path + "/" + FILENAME + ".csv", "w+") as baseFile:
            for row in strList:
                baseFile.write(str(row))

            baseFile.close()
            
        backupPath = path + "/backupCSV/"
        if (not os.path.exists(backupPath)):
            os.makedirs(backupPath)

        global currentBackup
        currentBackup = FILENAME + "_backup_" + str(math.floor(time.time()))

        with open(backupPath + "/" + currentBackup+ ".csv", "w+") as newFile:
            logging.info("Creating backup '" + currentBackup + ".csv'...")
            for row in strList:
                newFile.write(str(row))

            newFile.close()
            
        updateImport()
            
    except Exception as e:
        logging.error("Something went wrong when backing up")
        logging.error(e)


def updateDataset(current_accidents, import_set):
    """
    First reloads the accident data structure with the data from the importSet. Then, writes that data into the csv file.
    
    Parameters:
        current_accidents (dataset()): the current data structure holding the accidents data
        importSet (string): name of the csv file to import in the backupCSV/ folder
    """
    try:
        logging.info("Updating accident dataset...")
        global accidents
        del current_accidents

        # Reload accident dataset with imported data
        accidents = dataset(import_set)

        # Write over base dataset with imported data
        with open(os.path.abspath(os.path.dirname(__file__)) + "/" + FILENAME + ".csv", "w") as baseFile:
            for row in accidents.list:
                baseFile.write(",".join(row.toList()))

        baseFile.close()
    except Exception as e:
        logging.error(e)

def Import(importChoice):
    """
    The import functionality, which sets up and calls updateDataset with the backedup file
    """
    path = os.path.abspath(os.path.dirname(__file__))
    global accidents
    updateDataset(accidents, "/backupCSV/" + importChoice)

def heatmap(render):
    """
    heatmap of accidents in the US
    """
    pass

def Modify(request):
    """
    The main function for the insert, delete, modify, backup, and import functionality
    """
    try:
        # Inserting
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
                
                insertList = []
                latestRow = accidents.list[len(accidents.list) - 1]
                latestID = latestRow.ID.split("-")
                ID = "A-" + str(int(latestID[1]) + 1)
                insertList.extend((ID,str(severity), start_time, end_time, description, street, city, state))
                
                #TODO: Somehow insert this information into our file
                InsertRow(insertList)

        # Deleting
        elif (request.method == 'POST' and 'delete' in request.POST):
            #get user input
            form = DeleteForm(request.POST)
            #check if input is valid
            if form.is_valid():
                #grabs puts the user input into variables
                selection = form.cleaned_data['selection']
                search_text = form.cleaned_data['search_text']

                #delete all entries with id matching search_text
                if(selection == 'id'):
                    logging.info("delete by id")
                    DeleteRow(0, search_text)

                #delete all entries with city matching search_text
                elif(selection == 'city'):
                    logging.info("delete by city")
                    DeleteRow(13, search_text)

                #delete all entries with state matching search_text
                elif(selection == 'state'):
                    logging.info("delete by state")
                    DeleteRow(15, search_text)
        # Updating
        elif (request.method == 'POST' and 'update' in request.POST):
            # Get user input
            form = UpdateForm(request.POST)
            # Check if input is valid
            if form.is_valid():
                # Puts the user input into variables
                rowId = form.cleaned_data['id']
                updated_field = form.cleaned_data['updated_field']
                new_value = form.cleaned_data['new_value']

                # Update specified field with new_value
                if(updated_field == 'severity'):
                    logging.info('Update severity field')
                    if (accidents.updateRow(1, rowId, new_value, FILENAME)):
                        logging.info("Successfully updated severity field for ID "  + str(rowId))
                    else:
                        logging.info("ERROR: Could not update severity field for ID "  + str(rowId))

                elif(updated_field == 'start_time'):
                    logging.info('Update start_time')
                    if (accidents.updateRow(2, rowId, new_value, FILENAME)):
                        logging.info("Successfully updated start_time field for ID "  + str(rowId))
                    else:
                        logging.info("ERROR: Could not update start_time field for ID "  + str(rowId))

                elif(updated_field == 'end_time'):
                    logging.info('Update end_time')
                    if (accidents.updateRow(3, rowId, new_value, FILENAME)):
                        logging.info("Successfully updated end_time field for ID "  + str(rowId))
                    else:
                        logging.info("ERROR: Could not update end_time field for ID "  + str(rowId))

                elif(updated_field == 'description'):
                    logging.info('Update description')
                    if (accidents.updateRow(9, rowId, new_value, FILENAME)):
                        logging.info("Successfully updated description field for ID "  + str(rowId))
                    else:
                        logging.info("ERROR: Could not update description field for ID "  + str(rowId))

                elif(updated_field == 'street'):
                    logging.info('Update street')
                    if (accidents.updateRow(11, rowId, new_value, FILENAME)):
                        logging.info("Successfully updated street field for ID "  + str(rowId))
                    else:
                        logging.info("ERROR: Could not update street field for ID "  + str(rowId))

                elif(updated_field == 'city'):
                    logging.info('Update city')
                    if (accidents.updateRow(13, rowId, new_value, FILENAME)):
                        logging.info("Successfully updated city field for ID "  + str(rowId))
                    else:
                        logging.info("ERROR: Could not update city field for ID "  + str(rowId))

                elif(updated_field == 'state'):
                    logging.info('Update state')
                    if (accidents.updateRow(15, rowId, new_value, FILENAME)):
                        logging.info("Successfully updated state field for ID "  + str(rowId))
                    else:
                        logging.info("ERROR: Could not update state field for ID "  + str(rowId))

                path = os.path.abspath(os.path.dirname(__file__))
                strList = accidents.toList()

                with open(path + "/" + FILENAME + ".csv", "w+") as baseFile:
                    for row in strList:
                        baseFile.write(str(row))

                    baseFile.close()
                
        #if the backup button is clicked
        elif (request.method == 'POST' and 'backup' in request.POST):
            #TODO: create a backup when this button is clicked
            logging.info("Creating a backup...")
            Backup()
            update_scatter_plot(STATES_ABV)
        #if the import button is clicked
        elif (request.method == 'POST' and 'import' in request.POST):
            form = ImportForm(request.POST)
            if form.is_valid():
                logging.info("Importing from backup...")
                Import(str(form.cleaned_data['importChoice']))

    except Exception as e:
        logging.error(e)
    
    form = InsertForm()
    form2 = DeleteForm()
    form3 = UpdateForm()
    return render(request, "hello/modify.html", {'insert': form, 'delete': form2, 'update': form3})
