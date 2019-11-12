import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as snc
import matplotlib.gridspec as gridspec
import numpy as np
snc.set_style(style="darkgrid")

data = [28405,9693,52668,284103,1238823 ,0.03 ,0.419, 1.15,62.17,638.18 ,28405,418417,1036849,56409115,561519393  ]
labels = ["Diciembre", "Marzo" , "Junio" , "Septiembre" ,"Diciembre"]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars






def plots(x,data ,axs):
    axs.bar(x,data)
    axs.set(xlabel='Meses' , ylabel="Bs")
    axs.set_xticklabels(["Diciembre"]+labels, fontdict=None, minor=False)


fig = plt.figure(constrained_layout=True , figsize=(30,30))
spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)
ax1 = fig.add_subplot(spec2[0,0])
ax2 = fig.add_subplot(spec2[0,1])
ax3 = fig.add_subplot(spec2[1,0:])




plots(x,data[0:5],ax1)
plots(x,data[5:10],ax2)
plots(x,data[10:15] , ax3)

plt.show()


data= [[0,-66, 443,439,336],
    [0,1379, 132, 5306,927],
    [0,1373,148,5340,895]]

for i in range(3):
    plt.plot(x , data[i])
plt.legend(["Variacion de las Cuentas en efectivo en moneda nacional", "Variacion en Tipo de Cambio","Variacion de la Diferencia en Cambio"] )
plt.xticks(x, labels)
plt.show()
