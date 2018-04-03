import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("datos.txt")

plt.figure()
x=np.linspace(0,160,160)
plt.plot(data[:,0])
plt.plot(data[:,1])

plt.savefig("datosalbum.png")
plt.show()
