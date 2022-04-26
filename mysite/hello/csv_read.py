import os

class row_data:
	def __init__(self):
		return None
	
	def toList(self):
		tmp = [self.ID, self.severity, self.start_time, self.end_time, self.start_lat, self.start_lng, self.end_lat, self.end_lng, self.distance, self.description, self.number, self.street, self.side, self.city, self.county, self.state, self.zipcode, "US", self.timezone, self.airport_code, self.weather_timestamp, self.temperature, self.wind_chill, self.humidity, self.pressure, self.visibility, self.wind_direction, self.wind_speed, self.precipitation, self.weather_condition, "False", "False", self.crossing, "False", self.junction, "False", "False", "False", "False", "False", "False", self.traffic_signal, "False", self.sunrise_sunset, self.civil_twilight, self.nautical_twilight, self.astronomical_twilight]
		return tmp

class dataset:
	def __init__(self):
		self.list = []
		self.path = os.path.abspath(os.path.dirname(__file__))
		print("Opening csv file: US_Accidents_Dec21_updated.csv")

		with open(self.path + "/US_Accidents_Dec21_updated.csv", "r") as data:
			header = data.readline()
			for row in data:
				self.addRow(row.split(","))

			data.close()
		print("Done Reading csv file")

	def __init__(self, filename):
		self.list = []
		self.path = os.path.abspath(os.path.dirname(__file__))
		self.filename = filename

		print("Opening csv file: " + self.filename + ".csv")
		with open(self.path + "/" + self.filename + ".csv", "r") as data:
			self.header = data.readline()

			for row in data:
				self.addRow(row.split(","))

			data.close()
		print("Done Reading csv file")


	def addRow(self, line):
		tmp = row_data()

		tmp.ID = line[0]
		tmp.severity = line[1]
		tmp.start_time = line[2]
		tmp.end_time = line[3]
		tmp.start_lat = line[4]
		tmp.start_lng = line[5]
		tmp.end_lat = line[6]
		tmp.end_lng = line[7]
		tmp.distance = line[8]
		tmp.description = line[9]
		tmp.number = line[10]
		tmp.street = line[11]
		tmp.side = line[12]
		tmp.city = line[13]
		tmp.county = line[14]
		tmp.state = line[15]
		tmp.zipcode = line[16]
		tmp.timezone = line[18]
		tmp.airport_code = line[19]
		tmp.weather_timestamp = line[20]
		tmp.temperature = line[21]
		tmp.wind_chill = line[22]
		tmp.humidity = line[23]
		tmp.pressure = line[24]
		tmp.visibility = line[25]
		tmp.wind_direction = line[26]
		tmp.wind_speed = line[27]
		tmp.precipitation = line[28]
		tmp.weather_condition = line[29]
		tmp.crossing = line[32]
		tmp.junction = line[34]
		tmp.traffic_signal = line[41]
		tmp.sunrise_sunset = line[43]
		tmp.civil_twilight = line[44]
		tmp.nautical_twilight = line[45]
		tmp.astronomical_twilight = line[46]

		self.list.append(tmp)

	def removeRow(self, cmd, value):
		if (cmd == 0):
			for i in range(len(self.list)):
				if self.list[i].ID == value:
					del self.list[i]
					return 1

		elif (cmd == 13):
			tmp = []
			count = 0
			for row in self.list:
				if row.city != value:
					tmp.append(row)
				else:
					count += 1

			self.list = tmp
			return count

		elif (cmd == 15):
			tmp = []
			count = 0
			for row in self.list:
				if row.state != value:
					tmp.append(row)
				else:
					count += 1

			self.list = tmp
			return count

	def toList(self):
		tmp = []
		tmp.append(self.header)
		for row in self.list:
			tmp.append(",".join(row.toList()))

		return tmp

	def getRow(self, cmd, value):
		for row in self.list:
			if (cmd == 0):
				if row.ID == value:
					return row

			if (cmd == 1):
				if row.severity == value:
					return row

			elif (cmd == 2):
				if row.start_time == value:
					return row

			elif (cmd == 3):
				if row.end_time == value:
					return row

			# TODO: Change search to find a description LIKE the value
			elif (cmd == 9):
				if row.description == value:
					return row

			elif (cmd == 11):
				if row.street == value:
					return row

			elif (cmd == 13):
				if row.city == value:
					return row

			elif (cmd == 15):
				if row.state == value:
					return row

		# Return NoneType if nothing is found
		return None

	def updateRow(self, cmd, rowId, value, filename):
		# Get the row we want to change
		for i in range(len(self.list)):
			if self.list[i].ID == rowId:
				print("Found row!")
				# Then, change the specified column in the row
				if (cmd == 1):
					self.list[i].severity = value
				elif (cmd == 2):
					self.list[i].start_time = value
				elif (cmd == 3):
					self.list[i].end_time = value
				elif (cmd == 9):
					self.list[i].description = value
				elif (cmd == 11):
					self.list[i].street = value
				elif (cmd == 13):
					self.list[i].city = value
				elif (cmd == 15):
					self.list[i].state = value

				# Cast dataset into a list
				strList = self.toList()

				# Write out the list to the given file
				with open(self.path + "/" + filename + ".csv", "w+") as updateFile:
					for row in strList:
						updateFile.write(str(row))

					updateFile.close()

				# Return 1 to say that the row was updated
				return 1

		# Otherwise the row could not be found / updated
		return 0