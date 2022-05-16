import mpld3
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta
from .graph_plot import GraphPlot
from .graph_bar_hour import GraphHour
from .graph_bar_weather import GraphWeather

class Graphs():
	def __init__(self, accidents):
		self.path = os.path.abspath(os.path.dirname(__file__))
		self.plot = GraphPlot(accidents)
		self.barHour = GraphHour(accidents)
		self.barWeather = GraphWeather(accidents)

	def toHTML(self):
		mpld3Plot = mpld3.fig_to_html(self.plot.updateGraph())
		mpld3Hour = mpld3.fig_to_html(self.barHour.updateGraph())
		mpld3Weather = mpld3.fig_to_html(self.barWeather.updateGraph())

		HTML = f"""
			{{% extends './base.html' %}}
			{{%load static%}}

			{{% block title %}} Analytics {{% endblock %}}

			{{% block head %}}

			{{%endblock%}}

			{{%block body%}}
			<div>
				{mpld3Plot}
			</div>

			<div>
				{mpld3Hour}
			</div>

			<div>
				{mpld3Weather}
			</div>
			<div class = image-container>
				<img src="{{% static '/images/scatter_plot.png' %}}" alt="Crashes heatmap" width="90%" height="90%">
			</div>
			</body>

			{{%endblock%}}
			"""

		filename = open(self.path + "/templates/hello/analytics.html","w")
		filename.write(HTML)
		filename.close()
