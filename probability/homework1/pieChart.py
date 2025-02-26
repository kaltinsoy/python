import matplotlib
#matplotlib.use('TkAgg')  # Use Tkinter backend
import matplotlib.pyplot as plt
import numpy as np

ylabels = ["2021", "2022", "2023"]
y = np.array([1121, 1175, 1375])

plt.pie(y, labels = ylabels)

plt.title("KFAU data")
plt.savefig('pieChart.png', dpi=300, bbox_inches='tight')
plt.show()
