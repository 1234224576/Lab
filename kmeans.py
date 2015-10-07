# -*- coding: utf-8 -*-
from sklearn import neighbors
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt', delimiter=' ')
km = KMeans(n_clusters=3,init='random',n_init=1,verbose=1)
km.fit(data)

plot0_x = []
plot0_y = []
plot1_x = []
plot1_y = []
plot2_x = []
plot2_y = []
for label,data in zip(km.labels_,data):
	if label == 0:
		plot0_x.append(data[0])
		plot0_y.append(data[1])

	if label == 1:
		plot1_x.append(data[0])
		plot1_y.append(data[1])
		
	if label == 2:
		plot2_x.append(data[0])
		plot2_y.append(data[1])

plt.plot(plot0_x,plot0_y,"o")
plt.plot(plot1_x,plot1_y,"x")
plt.plot(plot2_x,plot2_y,"*")

plt.grid()
plt.show()
