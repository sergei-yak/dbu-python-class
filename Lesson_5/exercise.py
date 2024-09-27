#Scraping Data from a JSON API Source, Storing it in a CSV File, and Sorting by Columns

#Objective:

#Create a Python script using requests to retrieve data from a JSON API (e.g., weather data from Open-Meteo), store it in a CSV file, and sort the data by a specific column (e.g., temperature or wind speed).

#Pseudo Code:

#	1.	Send a Request to the API:

#	•	Use the requests library to send a GET request to the API.
#	2.	Check for a Successful Response:
#	•	Verify that the response’s status code is 200 (OK).
#	3.	Parse the JSON Data:
#	•	Convert the JSON response into a Python dictionary.
#	4.	Extract and Organize Data:
#	•	Extract relevant fields (e.g., temperature, humidity, wind speed) and organize them into a list of dictionaries for easier handling.
#	5.	Store Data in a CSV File:
#	•	Write the extracted data into a CSV file with appropriate headers (e.g., temperature, humidity, wind_speed).
#	6.	Sort Data by a Specific Column:
#	•	Sort the CSV data by a user-specified column (e.g., by temperature or wind_speed) before writing to the file.

import requests
import csv
import operator
import json

# API URL for weather data (Berlin, for example)
api_url = 'https://api.open-meteo.com/v1/forecast?latitude=32.7102759&longitude=-96.9470196&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

# Send request to the Open-Meteo API
response = requests.get(api_url)

# Check for successful response
if response.status_code == 200:
    data = response.json()
    # Save the data to a JSON file for further processing
    with open("Lesson_5/output/my_weather.json", 'w') as f:
        json.dump(data, f, indent=4)

# Parse the JSON Data:
# Load the weather data from the JSON file
with open("Lesson_5/output/my_weather.json", 'r') as f:
    data_dict = json.load(f)

#	•	Extract relevant fields (e.g., temperature, humidity, wind speed) and organize them into a list of dictionaries for easier handling.
date_time = data_dict['hourly']['time']
temp = data_dict['hourly']['temperature_2m']
humid = data_dict['hourly']['relative_humidity_2m']
wind_speed = data_dict['hourly']['wind_speed_10m']

#	•	Write the extracted data into a CSV file with appropriate headers (e.g., temperature, humidity, wind_speed).
csv_file = 'Lesson_5/output/my_weather_data.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    #the header
    writer.writerow(['date_time', 'temp', 'humid', 'wind_speed'])
    #the data in columns
    for i in range(len(date_time)):
        writer.writerow([date_time[i], temp[i], humid[i], wind_speed[i]])

#	•	Sort the CSV data by a user-specified column (e.g., by temperature or wind_speed) before writing to the file.
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Sort the data by the temp
sorted_data = sorted(data, key=lambda row: float(row['temp']))
for i in sorted_data:
    print(i)

