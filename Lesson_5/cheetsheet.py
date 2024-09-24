# How to use JSON in Python
import json

# Load JSON data from a string
data = json.loads('{"key": "value"}')

# Dump Python object to JSON string
json_str = json.dumps(data, indent=4)

# Load JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# Write Python object to a JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)


# How to use Matplotlib in Python for graphical visualization
import matplotlib.pyplot as plt

# Basic Line Plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

# Bar Chart
categories = ['A', 'B', 'C']
values = [3, 7, 5]
plt.bar(categories, values)
plt.title('Bar Chart')
plt.show()

# Pie Chart
sizes = [20, 30, 50]
labels = ['Group 1', 'Group 2', 'Group 3']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

# Scatter Plot
x = [5, 7, 8, 5, 6]
y = [7, 3, 2, 6, 8]
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.show()

# Save Plot as Image
plt.savefig('plot.png')


# How to use FPDF in Python for PDF generation
from fpdf import FPDF

# Create PDF Object
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font (Font family, style, size)
pdf.set_font('Arial', 'B', 16)

# Add a title
pdf.cell(200, 10, 'Title of the Document', ln=True, align='C')

# Add a new line
pdf.ln(10)

# Add regular text
pdf.set_font('Arial', '', 12)
pdf.cell(200, 10, 'This is a sample PDF document created with FPDF.', ln=True)

# Add multi-line text
text = 'This is a longer paragraph that will span multiple lines in the PDF.'
pdf.multi_cell(0, 10, text)

# Save the PDF to a file
pdf.output('sample.pdf')

# Adding an image
pdf.image('logo.png', x=10, y=8, w=33)