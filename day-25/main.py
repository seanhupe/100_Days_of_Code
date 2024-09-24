# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if (row[1]) != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
#import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data["temp"]))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # Calculate the Average Temp
# temp_average = sum(temp_list) / len(temp_list)
# print(round(temp_average, 2))
#     # Or...using Pandas
# print(data["temp"].mean())
#
# # Find the Maxium Temp
# print(data["temp"].max())
#
# # Get Data in Columns*
# print(data["condition"])
# print(data.condition)
# print(data["day"])
# print(data.day)
#
# # Get Data in an individual Row
# print(data[data.day == "Monday"])
# max_row = (data[data.day == "Monday"]).max()
#
# # Get the Row that has the Maximum Temperature
# print(data[data.temp == data.temp.max()])
#
# # Get Monday's temp, but convert to Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# dataframe_from_scratch = pandas.DataFrame(data_dict)
# print(dataframe_from_scratch)
# dataframe_from_scratch.to_csv("new_data.csv")

import pandas
