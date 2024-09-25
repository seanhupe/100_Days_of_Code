# with open("weather_data.csv") as data_file:
#     # Take data and put it into a list
#     data = data_file.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # Grabbing Temperature data in 2nd column and adding to temperatures list
#     temperatures = []
#     for row in data:
#         if (row[1]) != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
#
## USING PANDAS --------------------------------------------------------------------

import pandas

data = pandas.read_csv("weather_data.csv")
##This will show that the Temp column is known as a Series in Panda
# print(type(data["temp"]))
##This will print the Temperatures column
# print(data["temp"])
#
## This will convert the Weather.csv to a Dictionary
# data_dict = data.to_dict()
# print(data_dict)
#
## This will put the Temperatures into a list
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # Calculate the Average Temp
# temp_average = sum(temp_list) / len(temp_list)
# print(round(temp_average, 2))
#     # Or...using Pandas
# print(data["temp"].mean())
#
# # Find the Maximum Temp
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

## --------------------------------------------------------------------------------------------
#
# import pandas
# data = pandas.read_csv("squirrel_count.csv")                #importing & reading csv
# gray_squirrels = data[data["Primary Fur Color"] == "Gray"]  #get rows of gray squirrels
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])  #count of gray squirrels
# # print(gray_squirrels)
# print(gray_squirrels_count)
#
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])  #count of Cinnamon squirrels
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])  #count of Black squirrels
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# # Construct Dataframe
# ## 1st step is create the dictionary
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
# print(data_dict)
# ## 2nd step is turn the dictionary in to a Data Frame
# df = pandas.DataFrame(data_dict)
# ## Save the Data Frame into a new CSV file
# df.to_csv("squirrel_count_new")

