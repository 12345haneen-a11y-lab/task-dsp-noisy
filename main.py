import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)

xt = np.zeros_like(t)
xt[np.abs(t) < 0.01] = 1  # Impulse at t = 0

xt = np.heaviside(t, 1)
plt.plot(t, xt)
plt.title("unit step")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

