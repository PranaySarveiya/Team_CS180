import mpld3
import matplotlib.pyplot as plt
import os
from .graph_plot import GraphPlot
from .graph_bar_hour import GraphHour
from .graph_bar_weather import GraphWeather

class Graphs():
	def __init__(self, dataset, types):
		self.path = os.path.abspath(os.path.dirname(__file__))
		self.graphs = []
		self.figures = []
		self.getGraphs(dataset, types)

	def getGraphs(self, dataset, types):
		for graph in types:
			if graph == 0:
				plot = GraphPlot(dataset)
				self.graphs.append(plot)

			elif graph == 1:
				barHour = GraphHour(dataset)
				self.graphs.append(barHour)

			elif graph == 2:
				barWeather = GraphWeather(dataset)
				self.graphs.append(barWeather)

	def toFigures(self):
		for graph in self.graphs:
			self.figures.append(mpld3.fig_to_html(graph.updateGraph()))

	def toHTML(self):
		divs = ""
		self.toFigures()
		for figure in self.figures:
			divs += "<div>\n" + str(figure) + "</div>\n"

		HTML = f"""
			{{% extends './base.html' %}}
			{{%load static%}}

			{{% block title %}} Analytics {{% endblock %}}

			{{% block head %}}

			{{%endblock%}}

			{{%block body%}}
			{divs}
			<div class = image-container>
				<img src="{{% static '/images/scatter_plot.png' %}}" alt="Crashes heatmap" width="90%" height="90%">
			</div>
			</body>

			{{%endblock%}}
			"""

		filename = open(self.path + "/templates/hello/analytics.html","w")
		filename.write(HTML)
		filename.close()
