import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

# Simple Graph

x = [5, 8, 10]
y = [12, 16, 6]

x2 = [6, 9, 11]
y2 = [6, 15, 7]

plt.plot(x, y, 'g', label='line one', linewidth=5)
plt.plot(x2, y2, 'c', label='line two', linewidth=5)

plt.title('Simple Graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()
plt.grid(True, color='k')
plt.show()

# Bar Graph

plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="Example One", color='b')
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="Example Two", color='g')

plt.title('Bar Graph')
plt.ylabel('bar number')
plt.xlabel('bar height')
plt.show()

# Histogram
population_ages = [22, 55, 62, 45, 21, 22, 34,
                   42, 4, 99, 102, 110, 120, 115, 80, 75, 65]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.title('Histogram')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

# The main difference between Bar Graph and Histogram is:
# Histogram: Used when we are working with quantitave variables.
# Bar Graph: Used when we are working with categorical variabes.

# Chart / Pie Plot

slices = [6, 4, 13, 2]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),  # pull out a slice for 'eating' for example
        autopct='%1.1f%%')

plt.title('Chart')
plt.show()


# Scatter Plot
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]

plt.scatter(x, y, label='skitscat', color='k')
plt.title('Scatter Plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.show()

# Stack / Area Plot

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.plot([], [], color='m', label='Sleeping', linewidth=5)
plt.plot([], [], color='c', label='Eating', linewidth=5)
plt.plot([], [], color='r', label='Working', linewidth=5)
plt.plot([], [], color='k', label='Playing', linewidth=5)

plt.stackplot(days, sleeping, eating, working,
              playing, colors=['m', 'c', 'r', 'k'])

plt.title('Stack Plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.show()


# Multiple Plots


def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)


plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2))
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.show()
