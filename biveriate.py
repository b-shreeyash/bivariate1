import matplotlib.pyplot as plt

# Create a dictionary to store the productivity levels for different times of the day
productivity_levels = {
    "Morning": 5,
    "Midday": 4,
    "Afternoon": 3,
    "Evening": 2,
    "Night": 1
}

# Get the times of the day from the dictionary keys
times_of_day = list(productivity_levels.keys())

# Create a bar chart to visualize the productivity levels
plt.bar(times_of_day, productivity_levels.values())

# Set the chart title and labels
plt.title("Productivity Levels by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Productivity Level")

# Show the bar chart
plt.show()

# Check if the expected result holds true
expected_result = True
for i in range(len(times_of_day) - 1):
    if productivity_levels[times_of_day[i]] <= productivity_levels[times_of_day[i + 1]]:
        expected_result = False
        break

# Print the expected result
print("The expected result holds true:", expected_result)

