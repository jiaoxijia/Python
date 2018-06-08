import matplotlib as mpt
import numpy as np
from pylab import *
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S= np.cos(X),np.sin(X)

# print(C)
#创建一个8 * 6点（point）的图，并设置分辨率为 80
figure(figsize=(8,6), dpi=80)

subplot(1,1,1)
plot(X,C,color='blue',linewidth=1.0,linestyle="-")

plot(X,S, color='green',linewidth=1.0,linestyle='-')

xlim(-4.0,4.0)
xticks(np.linspace(-4,4,9,endpoint=True))

ylim(-1.0,1.0)

yticks(np.linspace(-1,1,5,endpoint=True))
show()
