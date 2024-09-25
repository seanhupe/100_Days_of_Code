## DICTIONARY COMPREHENSION

## formula:   new_dict ={new_key:new_value for item in list}
## formula:   new_dict ={new_key:new_value for (key,value) in dict.items()}
## formula:   new_dict ={new_key:new_value for (key,value) in dict.items() if test}

# ====================================================================================

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

## Create a dictionary where we generate a random score for each of the names
## formula:   new_dict ={new_key:new_value for item in list}
import random
students_scores ={student:random.randint(1, 100) for student in names}
print(students_scores)


## Create a Dictionary called 'passed_students' that looks through student_scores
## and find students that scored above 60
## passed_scores ={new_key:new_value for (key,value) in dictionary.items() if test}
passed_scores ={student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_scores)

# ====================================================================================
## CHALLENGE 1
## You are going to use Dictionary Comprehension to create a dictionary called result that takes
# each word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#result = {new_key:new_value for item in list}
result = {word: len(word) for word in sentence.split()}
print(result)


## CHALLENGE 2
## You are going to use Dictionary Comprehension to create a dictionary called weather_f that
## takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
## To convert temp_c into temp_f use this formula:
## (temp_c * 9/5) + 32 = temp_f

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# ={new_key:new_value for (key,value) in dictionary.items() if test}
weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)

# ====================================================================================

## How to use loops with Pandas DataFrames, and how to iterate over Panda DataFrame

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 75, 98]
}

# # Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key)
# for (key, value) in student_dict.items():
#     print(value)

import pandas

# Create DataFrame with Pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Looping through rows of the DataFrame , versus the column s
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
