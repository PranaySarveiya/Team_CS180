from django.test import TestCase
from .forms import InsertForm
from .views import accidents
from .views import InsertRow
import os

path = os.path.abspath(os.path.dirname(__file__))
filename = "US_Accidents_60000_rows"

# Create your tests here.
class InsertTest(TestCase):
    def setUp(self):
        self.accidents = accidents

    #test insertion of severity
    def test_Insert_severity(self):
        form = InsertForm(data = {"severity": 999, "start_time": "0:00:00", "end_time": "0:00:10","description": "test description", "street": "fake street", "city" : "riverside", "state" : "CA"})
        if form.is_valid():
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
            
            InsertRow(insertList) #takes a list of values to insert into file
            
            # Re-open the file to see if it was correctly updated
            with open(path + "/" + filename + ".csv", "r") as data:
                header = data.readline()
                for row in data:
                    # print(row[-1])
                    row = row.split(",")
                    if row[0] == ID:
                        print("Testing", ID, "severity insertion check")
                        self.assertEqual(row[1], str(severity))
                        break
                    
    #test insertion of severity                
    def test_Insert_start_time(self):
        form = InsertForm(data = {"severity": 999, "start_time": "0:00:00", "end_time": "0:00:10","description": "test description", "street": "fake street", "city" : "riverside", "state" : "CA"})
        if form.is_valid():
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
            
            InsertRow(insertList) #takes a list of values to insert into file
            
            # Re-open the file to see if it was correctly updated
            with open(path + "/" + filename + ".csv", "r") as data:
                header = data.readline()
                for row in data:
                    # print(row[-1])
                    row = row.split(",")
                    if row[0] == ID:
                        print("Testing", ID, "start_time insertion check")
                        self.assertEqual(row[2], start_time)
                        break
                    
    def test_Insert_end_time(self):
        form = InsertForm(data = {"severity": 999, "start_time": "0:00:00", "end_time": "0:00:10","description": "test description", "street": "fake street", "city" : "riverside", "state" : "CA"})
        if form.is_valid():
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
            
            InsertRow(insertList) #takes a list of values to insert into file
            
            # Re-open the file to see if it was correctly updated
            with open(path + "/" + filename + ".csv", "r") as data:
                header = data.readline()
                for row in data:
                    # print(row[-1])
                    row = row.split(",")
                    if row[0] == ID:
                        print("Testing", ID, "end_time insertion check")
                        self.assertEqual(row[3], end_time)
                        break
    
    def test_Insert_description(self):
        form = InsertForm(data = {"severity": 999, "start_time": "0:00:00", "end_time": "0:00:10","description": "test description", "street": "fake street", "city" : "riverside", "state" : "CA"})
        if form.is_valid():
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
            
            InsertRow(insertList) #takes a list of values to insert into file
            
            # Re-open the file to see if it was correctly updated
            with open(path + "/" + filename + ".csv", "r") as data:
                header = data.readline()
                for row in data:
                    # print(row[-1])
                    row = row.split(",")
                    if row[0] == ID:
                        print("Testing", ID, "description insertion check")
                        self.assertEqual(row[9], description)
                        break

    def test_Insert_street(self):
        form = InsertForm(data = {"severity": 999, "start_time": "0:00:00", "end_time": "0:00:10","description": "test description", "street": "fake street", "city" : "riverside", "state" : "CA"})
        if form.is_valid():
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
            
            InsertRow(insertList) #takes a list of values to insert into file
            
            # Re-open the file to see if it was correctly updated
            with open(path + "/" + filename + ".csv", "r") as data:
                header = data.readline()
                for row in data:
                    # print(row[-1])
                    row = row.split(",")
                    if row[0] == ID:
                        print("Testing", ID, "street insertion check")
                        self.assertEqual(row[11], street)
                        break
    def test_Insert_City(self):
        form = InsertForm(data = {"severity": 999, "start_time": "0:00:00", "end_time": "0:00:10","description": "test description", "street": "fake street", "city" : "riverside", "state" : "CA"})
        if form.is_valid():
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
            
            InsertRow(insertList) #takes a list of values to insert into file
            
            # Re-open the file to see if it was correctly updated
            with open(path + "/" + filename + ".csv", "r") as data:
                header = data.readline()
                for row in data:
                    # print(row[-1])
                    row = row.split(",")
                    if row[0] == ID:
                        print("Testing", ID, "City insertion check")
                        self.assertEqual(row[13], city)
                        break

    def test_Insert_State(self):
        form = InsertForm(data = {"severity": 999, "start_time": "0:00:00", "end_time": "0:00:10","description": "test description", "street": "fake street", "city" : "riverside", "state" : "CA"})
        if form.is_valid():
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
            
            InsertRow(insertList) #takes a list of values to insert into file
            
            # Re-open the file to see if it was correctly updated
            with open(path + "/" + filename + ".csv", "r") as data:
                header = data.readline()
                for row in data:
                    # print(row[-1])
                    row = row.split(",")
                    if row[0] == ID:
                        print("Testing", ID, "state insertion check")
                        self.assertEqual(row[15], state)
                        break