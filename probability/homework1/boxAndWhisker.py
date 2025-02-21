import matplotlib
matplotlib.use('TkAgg')  # Use Tkinter backend
import matplotlib.pyplot as plt
import numpy as np


depA = [7537, 11000, 12000, 13456, 34678, 34679, 35000, 35678, 36000, 36654]
depB = [8803, 8900 , 10345, 10999, 14556, 19000, 20678, 27689, 39000, 39639]
depC = [248, 441, 5678, 9008, 12345, 19234, 21000, 23567, 28056, 34590, 40000, 40475]

depT = [depA, depB, depC]

plt.boxplot(depT, patch_artist = True, labels = ["Departman A", "Departman B", "Departman C"])

plt.title("Box- and -Whisker Plot admittance to a university of 3 departments")
plt.ylabel("Values")
plt.xlabel("Departmans")

plt.show()
