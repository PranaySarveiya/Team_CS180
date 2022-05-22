import plotly.express as px

class GraphWeather():
	def __init__(self, accidents):
		self.accidents = accidents
		self.updateGraph()

	def updateGraph(self):
		## This snippet is to see all of the possible weather conditions
		#print("Rebuilding Bar Graph - Weather...")

		#allWeather = []
		#for row in accidents.list:
		#	allWeather.append(row.weather_condition)

		# uniqueWeather = set(allWeather)
		# print(uniqueWeather)

		# Creates a graph of accident counts for each of the listed weather conditions
		print("Rebuilding Bar Graph - Weather...")

		weather = ['Clear', 'Fair', 'Scattered Clouds', 'Smoke', 'Fog',  'Mist', 'Rain', 'Heavy Rain',  'Thunder', 'Snow']
		count = [0] * len(weather)
		for row in self.accidents.list:
			for i in range (0, len(weather)):
				if(weather[i] == row.weather_condition):
					count[i] += 1
					break

		self.fig = px.bar(x = weather, y = count,
			labels = dict(x = "Weather conditions", y = "Number of car accidents")	   
		)

		return self.fig
