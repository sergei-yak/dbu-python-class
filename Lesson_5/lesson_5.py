print('Hello world')
print('Hello again')
print('Hello once more')
import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Web_scraping")
bs = BeautifulSoup(response.text,"lxml")
print(bs.find("p").text)

#write the output to a file
with open("output.txt","w") as file:
    file.write(bs.find("p").text)

file.close()

import json

# API URL for weather data (Berlin, for example)
api_url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

# Fetch data from the API
response = requests.get(api_url)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()

    # Save the data to a JSON file for further processing
    with open("Output/weather_data.json", 'w') as f:
        json.dump(data, f, indent=4)

    print("Weather data fetched successfully!")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


#################
import matplotlib.pyplot as plt
from fpdf import FPDF

# Load the weather data from the JSON file
with open('Output/weather_data.json', 'r') as f:
    data = json.load(f)

# Extract the hourly data for temperature, humidity, and wind speed
hourly_data = data['hourly']
temperature = hourly_data['temperature_2m']
humidity = hourly_data['relative_humidity_2m']
wind_speed = hourly_data['wind_speed_10m']

# Time points (let's assume each hour corresponds to an index)
time_points = range(len(temperature))

# Create a function to generate graphs
def create_graphs():
    # Temperature plot
    plt.figure(figsize=(10, 5))
    plt.plot(time_points, temperature, label='Temperature (°C)', color='red')
    plt.xlabel('Time (Hours)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Over Time')
    plt.legend()
    plt.savefig("Output/temperature_plot.png")
    plt.close()

    # Humidity plot
    plt.figure(figsize=(10, 5))
    plt.plot(time_points, humidity, label='Relative Humidity (%)', color='blue')
    plt.xlabel('Time (Hours)')
    plt.ylabel('Relative Humidity (%)')
    plt.title('Humidity Over Time')
    plt.legend()
    plt.savefig("Output/humidity_plot.png")
    plt.close()

    # Wind speed plot
    plt.figure(figsize=(10, 5))
    plt.plot(time_points, wind_speed, label='Wind Speed (m/s)', color='green')
    plt.xlabel('Time (Hours)')
    plt.ylabel('Wind Speed (m/s)')
    plt.title('Wind Speed Over Time')
    plt.legend()
    plt.savefig("Output/wind_speed_plot.png")
    plt.close()

# Generate the graphs
create_graphs()

# Create a PDF report
pdf = FPDF()

# Add a page
pdf.add_page()

# Title
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Weather Data Report')

# Add text
pdf.set_font('Arial', '', 12)
pdf.ln(20)  # Line break
pdf.multi_cell(0, 10, "This report contains the weather data scraped from Open-Meteo API.")

# Add the temperature graph
pdf.ln(10)
pdf.cell(40, 10, 'Temperature Over Time:')
pdf.image("Output/temperature_plot.png", x=10, y=40, w=190)

# Add the humidity graph
pdf.add_page()
pdf.cell(40, 10, 'Humidity Over Time:')
pdf.image("Output/humidity_plot.png", x=10, y=40, w=190)

# Add the wind speed graph
pdf.add_page()
pdf.cell(40, 10, 'Wind Speed Over Time:')
pdf.image("Output/wind_speed_plot.png", x=10, y=40, w=190)

# Save the PDF
pdf.output("Output/weather_report.pdf")

print("Weather report PDF generated successfully!")


