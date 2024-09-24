# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if (row[1]) != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# Calculate the Average Temp
temp_average = sum(temp_list) / len(temp_list)
print(round(temp_average, 2))
    # Or...using Pandas
print(data["temp"].mean())
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])

