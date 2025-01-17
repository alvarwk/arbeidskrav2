import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)

y = -x**2 - 5

plt.plot(x, y, label='$f(x) = -x^2 - 5$', color='r')

plt.title('Plot av funksjonen $f(x) = -x^2 - 5$')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.legend()
plt.show()
