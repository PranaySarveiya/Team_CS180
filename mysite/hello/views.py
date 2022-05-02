from django.shortcuts import render
from django.http import HttpResponse
from hello.csv_read import dataset
from .forms import SearchForm
from .forms import InsertForm
from .forms import DeleteForm
from .forms import UpdateForm
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
FILENAME = "US_Accidents_60000_rows"
CURRENT_BACKUP = ""
ACCIDENTS = dataset(FILENAME)



def welcome(request):
    """
    The first page you see when you enter the website
    """
    return render(request, "hello/welcome.html")

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
        for row in ACCIDENTS.list:
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
        for row in ACCIDENTS.list:
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
        total = len(ACCIDENTS.list)
        logging.info("total entries:", total)
        stateCount = [0] * 51
        percent = [0] * 51

        s_time = time.time()
        for row in ACCIDENTS.list:
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
        count = ACCIDENTS.removeRow(column, value)

        # Now write the changed dataset to the base file
        path = os.path.abspath(os.path.dirname(__file__))
        strList = ACCIDENTS.toList()

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
            dataWrite.write(csv_string + "\n") #write to file

            ACCIDENTS.addRow(csv_string.split(",")) #add to data structure

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
        str_list = ACCIDENTS.toList()

        with open(path + "\\" + FILENAME + ".csv", "w+") as base_file:
            for row in str_list:
                base_file.write(str(row))

            base_file.close()
            
        backupPath = path + "/backupCSV/"
        if (not os.path.exists(backupPath)):
            os.makedirs(backupPath)

        global CURRENT_BACKUP
        CURRENT_BACKUP = FILENAME + "_backup_" + str(math.floor(time.time()))

        with open(backupPath + "/" + CURRENT_BACKUP + ".csv", "w+") as new_file:
            logging.info("Creating backup '" + CURRENT_BACKUP + ".csv'...")
            for row in str_list:
                new_file.write(str(row))

            new_file.close()
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
        global ACCIDENTS
        del current_accidents

        # Reload accident dataset with imported data
        ACCIDENTS = dataset(import_set)

        # Write over base dataset with imported data
        with open(os.path.abspath(os.path.dirname(__file__)) + "/" + FILENAME + ".csv", "w") as baseFile:
            for row in ACCIDENTS.list:
                baseFile.write(",".join(row.toList()))

        baseFile.close()
    except Exception as e:
        logging.error(e)


def Import():
    """The import functionality, which sets up and calls updateDataset with the backedup file"""
    path = os.path.abspath(os.path.dirname(__file__))
    global ACCIDENTS, CURRENT_BACKUP
    updateDataset(ACCIDENTS, "/backupCSV/" + CURRENT_BACKUP)
        

def Modify(request):
    """
    The main function for the insert, delete, modify, backup, and import functionality
    """
    try:        
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
                
                insert_list = []
                latestRow = ACCIDENTS.list[len(ACCIDENTS.list) - 1]
                latest_ID = latestRow.ID.split("-")
                ID = "A-" + str(int(latest_ID[1]) + 1)
                insert_list.extend((ID,str(severity), start_time, end_time, description, street, city, state))
                
                #TODO: Somehow insert this information into our file
                InsertRow(insert_list)

        #deleting
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
        #updating
        elif (request.method == 'POST' and 'update' in request.POST):
            # Get user input
            form = UpdateForm(request.POST)
            #check if input is valid
            if form.is_valid():
                # Puts the user input into variables
                row_Id = form.cleaned_data['id']
                updated_field = form.cleaned_data['updated_field']
                new_value = form.cleaned_data['new_value']

                # Update specified field with new_value
                if(updated_field == 'severity'):
                    logging.info('Update severity field')
                    if (ACCIDENTS.updateRow(1, row_Id, new_value, FILENAME)):
                        logging.info("Successfully updated severity field for ID "  + str(row_Id))
                    else:
                        logging.warning("ERROR: Could not update severity field for ID "  + str(row_Id))

                elif(updated_field == 'start_time'):
                    logging.info('Update start_time')
                    if (ACCIDENTS.updateRow(2, row_Id, new_value, FILENAME)):
                        logging.info("Successfully updated start_time field for ID "  + str(row_Id))
                    else:
                        logging.warning("ERROR: Could not update start_time field for ID "  + str(row_Id))

                elif(updated_field == 'end_time'):
                    logging.info('Update end_time')
                    if (ACCIDENTS.updateRow(3, row_Id, new_value, FILENAME)):
                        logging.info("Successfully updated end_time field for ID "  + str(row_Id))
                    else:
                        logging.warning("ERROR: Could not update end_time field for ID "  + str(row_Id))

                elif(updated_field == 'description'):
                    logging.info('Update description')
                    if (ACCIDENTS.updateRow(9, row_Id, new_value, FILENAME)):
                        logging.info("Successfully updated description field for ID "  + str(row_Id))
                    else:
                        logging.warning("ERROR: Could not update description field for ID "  + str(row_Id))

                elif(updated_field == 'street'):
                    logging.info('Update street')
                    if (ACCIDENTS.updateRow(11, row_Id, new_value, FILENAME)):
                        logging.info("Successfully updated street field for ID "  + str(row_Id))
                    else:
                        logging.warning("ERROR: Could not update street field for ID "  + str(row_Id))

                elif(updated_field == 'city'):
                    logging.info('Update city')
                    if (ACCIDENTS.updateRow(13, row_Id, new_value, FILENAME)):
                        logging.info("Successfully updated city field for ID "  + str(row_Id))
                    else:
                        logging.warning("ERROR: Could not update city field for ID "  + str(row_Id))

                elif(updated_field == 'state'):
                    logging.info('Update state')
                    if (ACCIDENTS.updateRow(15, row_Id, new_value, FILENAME)):
                        logging.info("Successfully updated state field for ID "  + str(row_Id))
                    else:
                        logging.warning("ERROR: Could not update state field for ID "  + str(row_Id))
                
        #if the backup button is clicked
        elif (request.method == 'POST' and 'backup' in request.POST):
            #TODO: create a backup when this button is clicked
            logging.info("Creating a backup...")
            Backup()
        #if the import button is clicked
        elif (request.method == 'POST' and 'import' in request.POST):
            #TODO: implement importing stuff
            logging.info("Importing from backup...")
            Import()
    except Exception as e:
        logging.error(e)
    
    form = InsertForm()
    form2 = DeleteForm()
    form3 = UpdateForm()
    return render(request, "hello/modify.html", {'insert': form, 'delete': form2, 'update': form3})