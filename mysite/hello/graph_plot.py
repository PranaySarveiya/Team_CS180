from .graph_base import Graph
from datetime import datetime
import plotly.express as px

class GraphPlot(Graph):
	def __init__(self, dataset):
		super().__init__(dataset)

	def updateGraph(self):
		year = 2016
		month = 1
		day = 1

		dateformat = "%Y-%m-%d"
		currentDate = datetime(year, month, day)

		print("Rebuilding Plot Graph - Month...")
		# Iterate through all dates between 2016 to the start of 2022
		count = [0] * 72
		mult = 0

		for row in self.dataset.list:
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
					count[date.month - 1] += 1
			else:
					count[(date.month - 1) + (12 * mult)] += 1

		months = []
		year = 2016
		for i in range(1, 73):
			if (i % 12 == 0):
				tmp = datetime(year, 12, 1)
				months.append(tmp.strftime("%b %y"))
				year += 1
			else:
				tmp = datetime(year, i % 12, 1)
				months.append(tmp.strftime("%b %y"))

		self.fig = px.line(x = months, y = count,
			labels = dict(x = "Month of crash", y = "Number of car accidents")	
		)

		self.fig.update_layout(
			autosize = True,
			margin = dict(
				l = 300,
				r = 300,
				b = 0,
				t = 50
			),
		)

		return self.fig
