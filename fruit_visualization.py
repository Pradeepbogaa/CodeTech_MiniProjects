import matplotlib.pyplot as plt

# Sample data for pie chart
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [30, 40, 15, 15]

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Fruit Distribution")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()

# Sample data for bar graph
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 15, 30, 20]

# Create a bar graph
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue')
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Graph Example")
plt.show()
