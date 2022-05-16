import matplotlib.pyplot as plt

class GraphWeather():
	def __init__(self, accidents):
		self.figure = plt.figure(figsize = (18,8))
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

		weathers = ['Clear', 'Fair', 'Scattered Clouds', 'Smoke', 'Fog',  'Mist', 'Rain', 'Heavy Rain',  'Thunder', 'Snow']
		counts = [0] * len(weathers)
		for row in self.accidents.list:
			for i in range (0, len(weathers)):
				if(weathers[i] == row.weather_condition):
					counts[i] += 1
					break

		fig, ax = plt.subplots(figsize=(18, 8))
		bars = ax.bar(weathers, counts)
		ax.bar_label(bars)


		for bars in ax.containers:
			ax.bar_label(bars)

		plt.xlabel("Weather conditions")
		plt.ylabel("Number of car accidents")
		plt.title('Car Crashes by Weather Condition')

		return fig
