from .graph_base import Graph
import plotly.express as px

class GraphHour(Graph):
	def __init__(self, dataset):
		super().__init__(dataset)

	def updateGraph(self):
		# Getting plot of the car accident counts by the hour
		print("Rebuilding Bar Graph - Hour...")

		hours = list(range(0, 24))
		count = [0] * 24
		for row in self.dataset.list:
			hour = row.start_time.split(" ")[1].split(":")[0]
			count[int(hour)] += 1
		

		self.fig = px.bar(x = hours, y = count,
			labels = dict(x = "Hour", y = "Number of car accidents")	   
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
