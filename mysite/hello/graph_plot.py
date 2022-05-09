if __name__ == '__main__':
	from csv_read import dataset

	filename = "US_Accidents_60000_rows"
	accidents = dataset(filename)

	import matplotlib.pyplot as plt
	from datetime import datetime, timedelta

	year = 2016
	month = 1
	day = 1

	dates = []
	dateformat = "%Y-%m-%d"
	currentDate = datetime(year, month, day)

	print("Building date count. This will take a while...")
	# Iterate through all dates between 2016 to the start of 2022
	dates = [0] * 72
	mult = 0
	x = []

	for row in accidents.list:
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
			x.append(str(year) + "-12-1")
			year += 1
		else:
			x.append(str(year) + "-" + str(i % 12) + "-1")

	# Display the data as a graph
	plt.plot(x, dates)
	plt.xlabel('Month of crash')
	plt.ylabel('Amount of crashes per month')
	plt.title('Car Crashes per month 2016 - 2021')
	plt.show()

	# #getting plot of the car accident counts by the hour#########################################################################################
	# hours = list(range(0, 24))
	
	# count = [0] * 24
	# for row in accidents.list:
	# 	hour = row.start_time.split(" ")[1].split(":")[0]
	# 	count[int(hour)] += 1
		
		

	# fig, ax = plt.subplots()
	# bars = ax.bar(hours, count)
	# ax.bar_label(bars)
	# ax.set_xticks(hours)

	# for bars in ax.containers:
	# 	ax.bar_label(bars)
	# plt.xlabel("Hours")
	# plt.ylabel("Number of car accidents")
	# plt.title('Car Crashes by Hours')
	# plt.show()

# #this snippet is to see all of the possible weather conditions#####################################################################################
# allWeather = []
# for row in accidents.list:
# 	allWeather.append(row.weather_condition)
# uniqueWeather = set(allWeather)
# print(uniqueWeather)

#creates a graph of accident counts for each of the listed weather conditions#####################################################################

# weathers = ['Clear', 'Fair', 'Scattered Clouds', 'Smoke', 'Fog',  'Mist', 'Rain', 'Heavy Rain',  'Thunder', 'Snow']
# counts = [0] * len(weathers)
# for row in accidents.list:
# 	for i in range (0, len(weathers)):
# 		if(weathers[i] == row.weather_condition):
# 			counts[i] += 1
# 			break

# fig, ax = plt.subplots()
# bars = ax.bar(weathers, counts)
# ax.bar_label(bars)


# for bars in ax.containers:
# 	ax.bar_label(bars)
# plt.xlabel("Weather conditions")
# plt.ylabel("Number of car accidents")
# plt.title('Car Crashes by Weather Condition')
# plt.show()	
