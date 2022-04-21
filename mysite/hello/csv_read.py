import os

class row_data:
	def __init__(self):
		return None

class dataset:
	def __init__(self):
		self.list = []
		self.path = os.path.abspath(os.path.dirname(__file__))
		print("Opening csv file")
		with open(self.path + "/US_Accidents_Dec21_updated.csv", "r") as data:
			header = data.readline()
			# cnt = 0
			for row in data:
				self.addRow(row.split(","))
				# cnt += 1
				# if(cnt == 1300000):
				# 	break
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
		tmp.Precipitation = line[28]
		tmp.Weather_Condition = line[29]
		tmp.Crossing = line[32]
		tmp.Junction = line[34]
		tmp.Traffic_Signal = line[41]
		tmp.Sunrise_Sunset = line[43]
		tmp.Civil_Twilight = line[44]
		tmp.Nautical_Twilight = line[45]
		tmp.Astronomical_Twilight = line[46]

		self.list.append(tmp)

	def getRow(self):
		return self.list[0]