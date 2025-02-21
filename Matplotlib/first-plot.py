# Matplotlib

from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
dev_y = [38000, 35577, 33154, 30731, 28308, 25885, 23462, 21039, 18616, 16193]
py_dev_y = [40000, 43000, 45000, 48000, 54000, 62000, 74000, 76000, 85000, 94000]

# plot the data
# x and y
plt.plot(ages_x, dev_y)

# Add some descriptions for the data
plt.title("Median salary (USD) by age")


# Another plot
plt.plot(ages_x, py_dev_y)

 
# X and Y labels
plt.xlabel("Ages")
plt.ylabel("USD")

# Show the plot
plt.show()