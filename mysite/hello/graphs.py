from .graph_plot import GraphPlot
from .graph_bar_hour import GraphHour
from .graph_bar_weather import GraphWeather
from bs4 import BeautifulSoup
import os
import plotly

class Graphs():
	def __init__(self, dataset, types):
		self.path = os.path.abspath(os.path.dirname(__file__))
		self.graphs = []
		self.getGraphs(dataset, types)

	def getGraphs(self, dataset, types):
		for graph in types:
			if graph == "plot":
				plot = GraphPlot(dataset)
				self.graphs.append(plot)

			elif graph == "bar hour":
				barHour = GraphHour(dataset)
				self.graphs.append(barHour)

			elif graph == "bar weather":
				barWeather = GraphWeather(dataset)
				self.graphs.append(barWeather)

	def toHTML(self):
		divs = ""
		for graph in self.graphs:
			soup = BeautifulSoup(plotly.io.to_html(graph.updateGraph()), features="html.parser")
			divs += "<div>\n" + str(soup.findAll('div')) + "</div>\n"

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
