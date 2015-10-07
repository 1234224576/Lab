import numpy as np
from matplotlib.pyplot import show
from scipy.cluster.hierarchy import ward, dendrogram

data = np.loadtxt('data.txt', delimiter=' ')
result1 = ward(data)
dendrogram(result1)
show()