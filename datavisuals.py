import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3]
y = [0,2,4,6]

plt.plot(x, y, 'b^-', label = '2x')
plt.title("Graph1", fontdict={'fontname': 'Ariel','fontsize':20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8,10])

plt.legend()

plt.show()