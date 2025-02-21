import matplotlib
matplotlib.use('TkAgg')  # Use Tkinter backend
import matplotlib.pyplot as plt
#import numpy as np

ylabels = ["2021", "2022", "2023"]
y = [1121, 1175, 1375]

plt.bar(ylabels, y)

plt.title("KFAU data")
plt.xlabel("Years")
plt.ylabel("Student total")
plt.show()
