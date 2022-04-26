from django.test import TestCase
from .forms import UpdateForm
from .views import accidents
import os

path = os.path.abspath(os.path.dirname(__file__))
filename = "US_Accidents_60000_rows"

# Create your tests here.
class UpdateTest(TestCase):
	def setUp(self):
		print("Reloading accidents data structure")
		self.accidents = accidents

	# Test severity update
	def test_update_severity(self):
		# Cast the data as a form
		form = UpdateForm(data = {"id": "A-1", "updated_field": "severity", "new_value": "4", "update": ""})
		
		if form.is_valid():
			# Get the data
			rowId = form.cleaned_data['id']
			updated_field = form.cleaned_data['updated_field']
			new_value = form.cleaned_data['new_value']
		
			# Update the file with the changed data
			if (self.accidents.updateRow(1, rowId, new_value, filename)):
				# Re-open the file to see if it was correctly updated
				with open(path + "/" + filename + ".csv", "r") as data:
					header = data.readline()
					for row in data:
						row = row.rstrip("\n").split(",")

						if row[0] == rowId:
							# See if the severity column was changed
							self.assertEqual(row[1], new_value)
							break

	# Test start_time update
	def test_update_start_time(self):
		# Cast the data as a form
		form = UpdateForm(data = {"id": "A-21", "updated_field": "start_time", "new_value": "2022-04-25 19:17:00", "update": ""})
		
		if form.is_valid():
			# Get the data
			rowId = form.cleaned_data['id']
			updated_field = form.cleaned_data['updated_field']
			new_value = form.cleaned_data['new_value']
		
			# Update the file with the changed data
			if (self.accidents.updateRow(2, rowId, new_value, filename)):
				# Re-open the file to see if it was correctly updated
				with open(path + "/" + filename + ".csv", "r") as data:
					header = data.readline()
					for row in data:
						row = row.rstrip("\n").split(",")

						if row[0] == rowId:
							# See if the start_date column was changed
							self.assertEqual(row[2], new_value)
							break

	# Test end_time update
	def test_update_end_time(self):
		# Cast the data as a form
		form = UpdateForm(data = {"id": "A-265", "updated_field": "end_time", "new_value": "2022-04-26 12:23:45", "update": ""})
		
		if form.is_valid():
			# Get the data
			rowId = form.cleaned_data['id']
			updated_field = form.cleaned_data['updated_field']
			new_value = form.cleaned_data['new_value']
		
			# Update the file with the changed data
			if (self.accidents.updateRow(3, rowId, new_value, filename)):
				# Re-open the file to see if it was correctly updated
				with open(path + "/" + filename + ".csv", "r") as data:
					header = data.readline()
					for row in data:
						row = row.rstrip("\n").split(",")

						if row[0] == rowId:
							# See if the end_date column was changed
							self.assertEqual(row[3], new_value)
							break

	# Test description update
	def test_update_description(self):
		# Cast the data as a form
		form = UpdateForm(data = {"id": "A-1193", "updated_field": "description", "new_value": "On the 215 South ramp", "update": ""})
		
		if form.is_valid():
			# Get the data
			rowId = form.cleaned_data['id']
			updated_field = form.cleaned_data['updated_field']
			new_value = form.cleaned_data['new_value']
		
			# Update the file with the changed data
			if (self.accidents.updateRow(9, rowId, new_value, filename)):
				# Re-open the file to see if it was correctly updated
				with open(path + "/" + filename + ".csv", "r") as data:
					header = data.readline()
					for row in data:
						row = row.rstrip("\n").split(",")

						if row[0] == rowId:
							# See if the end_date column was changed
							self.assertEqual(row[9], new_value)
							break

	# Test street update
	def test_update_street(self):
		# Cast the data as a form
		form = UpdateForm(data = {"id": "A-331", "updated_field": "street", "new_value": "Texas Ave.", "update": ""})
		
		if form.is_valid():
			# Get the data
			rowId = form.cleaned_data['id']
			updated_field = form.cleaned_data['updated_field']
			new_value = form.cleaned_data['new_value']
		
			# Update the file with the changed data
			if (self.accidents.updateRow(11, rowId, new_value, filename)):
				# Re-open the file to see if it was correctly updated
				with open(path + "/" + filename + ".csv", "r") as data:
					header = data.readline()
					for row in data:
						row = row.rstrip("\n").split(",")

						if row[0] == rowId:
							# See if the end_date column was changed
							self.assertEqual(row[11], new_value)
							break

	# Test street update
	def test_update_city(self):
		# Cast the data as a form
		form = UpdateForm(data = {"id": "A-100", "updated_field": "city", "new_value": "Riverside", "update": ""})
		
		if form.is_valid():
			# Get the data
			rowId = form.cleaned_data['id']
			updated_field = form.cleaned_data['updated_field']
			new_value = form.cleaned_data['new_value']
		
			# Update the file with the changed data
			if (self.accidents.updateRow(13, rowId, new_value, filename)):
				# Re-open the file to see if it was correctly updated
				with open(path + "/" + filename + ".csv", "r") as data:
					header = data.readline()
					for row in data:
						row = row.rstrip("\n").split(",")

						if row[0] == rowId:
							# See if the end_date column was changed
							self.assertEqual(row[13], new_value)
							break

	# Test state update
	def test_update_state(self):
		# Cast the data as a form
		form = UpdateForm(data = {"id": "A-99", "updated_field": "state", "new_value": "OH", "update": ""})
		
		if form.is_valid():
			# Get the data
			rowId = form.cleaned_data['id']
			updated_field = form.cleaned_data['updated_field']
			new_value = form.cleaned_data['new_value']
		
			# Update the file with the changed data
			if (self.accidents.updateRow(15, rowId, new_value, filename)):
				# Re-open the file to see if it was correctly updated
				with open(path + "/" + filename + ".csv", "r") as data:
					header = data.readline()
					for row in data:
						row = row.rstrip("\n").split(",")

						if row[0] == rowId:
							# See if the end_date column was changed
							self.assertEqual(row[15], new_value)
							break
