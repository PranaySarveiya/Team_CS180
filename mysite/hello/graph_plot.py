import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class GraphPlot():
	def __init__(self, accidents):
		self.figure = plt.figure(figsize = (18,8))
		self.accidents = accidents
		self.updateGraph()

	def updateGraph(self):
		year = 2016
		month = 1
		day = 1

		dates = []
		dateformat = "%Y-%m-%d"
		currentDate = datetime(year, month, day)

		print("Rebuilding Plot Graph - Month...")
		# Iterate through all dates between 2016 to the start of 2022
		dates = [0] * 72
		mult = 0
		x = []

		for row in self.accidents.list:
			date = datetime.strptime(row.start_time.split(" ")[0], dateformat)

			if (date.year == 2017):
				mult = 1
			elif (date.year == 2018):
				mult = 2
			elif (date.year == 2019):
				mult = 3
			elif (date.year == 2020):
				mult = 4
			elif (date.year == 2021):
				mult = 5

			if (date.year == 2016):
					dates[date.month - 1] += 1
			else:
					dates[(date.month - 1) + (12 * mult)] += 1

		x = []
		year = 2016
		for i in range(1, 73):
			if (i % 12 == 0):
				tmp = datetime(year, 12, 1)
				x.append(tmp.strftime("%b\n%y"))
				year += 1
			else:
				tmp = datetime(year, i % 12, 1)
				x.append(tmp.strftime("%b\n%y"))

		# Display the data as a graph
		plt.plot(x, dates)
		plt.xlabel('Month of crash')
		plt.ylabel('Amount of crashes per month')
		plt.title('Car Crashes per month 2016 - 2021')

		return self.figure
