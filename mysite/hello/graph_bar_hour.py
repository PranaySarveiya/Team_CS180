import matplotlib.pyplot as plt

class GraphHour:
	def __init__(self, accidents):
		self.figure = plt.figure(figsize = (18,8))
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
		
		

		fig, ax = plt.subplots(figsize=(18, 8))
		bars = ax.bar(hours, count)
		ax.bar_label(bars)
		ax.set_xticks(hours)

		for bars in ax.containers:
			ax.bar_label(bars)

		plt.xlabel("Hours")
		plt.ylabel("Number of car accidents")
		plt.title('Car Crashes by Hours')

		return fig
