import plotly.express as px

class GraphHour:
	def __init__(self, accidents):
		self.accidents = accidents
		self.updateGraph()

	def updateGraph(self):
		# Getting plot of the car accident counts by the hour
		print("Rebuilding Bar Graph - Hour...")

		hours = list(range(0, 24))
		count = [0] * 24
		for row in self.accidents.list:
			hour = row.start_time.split(" ")[1].split(":")[0]
			count[int(hour)] += 1
		

		self.fig = px.bar(x = hours, y = count,
			labels = dict(x = "Hour", y = "Number of car accidents")	   
		)

		return self.fig
