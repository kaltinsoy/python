import matplotlib
#matplotlib.use('TkAgg')  # Use Tkinter backend
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.DataFrame({'testx': ["2021", "2022", "2023"],
                          'testy': [1121, 1175, 1375]})

plt.plot(dataframe.testx, dataframe.testy)

plt.title("KFAU data")


plt.xlabel("Years")
plt.ylabel("Total student")

plt.savefig('plot.png', dpi=300, bbox_inches='tight')

plt.show()  # Display the plot
