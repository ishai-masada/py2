import matplotlib.pyplot as pyplot
import seaborn
import numpy

x_values = [num for num in range(7)]
y_values = [num for num in range(7)]

seaborn.lineplot(x=x_values, y=y_values)
pyplot.show()

time = numpy.arange(0, 20, 1)
pyplot.plot(time, numpy.sin(time))
pyplot.show()
