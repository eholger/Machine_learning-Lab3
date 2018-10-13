import matplotlib.pyplot as plt
import numpy as np



error = [i/float(100) for i in range(1,100)]

plt.plot([0.5*(np.log(1-e)-np.log(e)) for e in error])
plt.show()


