import csv

import matplotlib.pyplot as plt

filename = 'data/jackson_heights_weather_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, column_header in enumerate(header_row):
		print(index, column_header)
		
	
	# Get dates from this file.
	dates = []
	for row in reader:
		date = int(row[4])
		dates.append(date)

print(dates)

# Plot the dates.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, c='red')

# Format plot.
plt.title("Dates, 2023", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Date", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()