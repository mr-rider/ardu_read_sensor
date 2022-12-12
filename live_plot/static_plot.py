# static_plot.py

# import necessary packages
import matplotlib.pyplot as plt

# data
data_lst = [30, 25, 10, 41, 33, 1, 5, 10, 41]

# create the figure and axis objects
fig, ax = plt.subplots()

# plot the data and customize
ax.plot(data_lst)
ax.set_xlabel('Day number')
ax.set_ylabel('Temperature (*C)')
ax.set_title('Temperute in Italy, OR over 7 days')

# save and show the plot
fig.savefig('static_plot.png')
plt.show()
