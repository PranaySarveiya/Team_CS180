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
	while(currentDate.year != 2022):
		count = 0

		# Show at least some progress
		if (currentDate.year != year):
			year += 1
			print(currentDate.year)

		# Iterate through the entire list... for every date
		for crash in accidents.list:
			date = datetime.strptime(crash.start_time.split(" ")[0], dateformat)

			if (date == currentDate):
				count += 1

		dates.append([currentDate, count])
		currentDate += timedelta(days = 1)

	# Split the list into explicitly dates or count
	x = []
	y = []
	for item in dates:
		x.append(item[0])
		y.append(item[1])

	# Display the data as a graph
	plt.plot(x, y)
	plt.xlabel('Date of crash')
	plt.ylabel('Amount of crashes')
	plt.title('Car Crashes 2016 - 2021')
	plt.show()