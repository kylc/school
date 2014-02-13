import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data.csv', delimiter=',', names=['size', 'time'])

plt.loglog(data['size'], data['time'])

slope, intercept = np.polyfit(np.log(data['size']), np.log(data['time']), 1)
print slope

plt.title("Algorithm")
plt.xlabel("Input Size")
plt.ylabel("Time (s)")
plt.show()
