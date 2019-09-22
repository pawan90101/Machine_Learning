#in a jupyter notbook there are problem to live demo so we are using normal file to this.
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import csv
plt.style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def animate(p):
    plot_data = open('D:/Pycharm/MatPlotLib/sample.csv','r')
    line_data = csv.reader(plot_data)
    x1=[]
    y1=[]
    for line in line_data:
        if(len(line)>1):
            x1.append(line[0])
            y1.append(line[1])
        ax1.clear()
        ax1.plot(x1,y1)

animate_data = animation.FuncAnimation(fig,animate,interval=500)
plt.show()
