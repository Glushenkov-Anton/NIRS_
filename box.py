import pandas as pd
import matplotlib.pyplot as plt
import statistics

data = pd.read_excel('mass_sorted.xlsx')
A = data[data["Страна"] == "Европа"]["Емкость"]
Aavg = sum(A)/len(A)
Aerr = statistics.stdev(A)
B = data[data["Страна"] == "Азия"]["Емкость"]
Bavg = sum(B)/len(B)
Berr = statistics.stdev(B)

list = ['Европа', 'Азия']
listAVG = [Aavg, Bavg]
listERR = [Aerr/2, Berr/2]
print(list, listAVG)

plt.errorbar(x=list, y=listAVG, yerr=listERR, color="black", capsize=3, marker="s", markersize=5, mfc="red", mec="black", fmt='o')
plt.title('Емкость аккумулятора для различных стран-производителей')
plt.grid()
plt.xlabel('Страна-производитель')
plt.ylabel('Емкость')
plt.show()
