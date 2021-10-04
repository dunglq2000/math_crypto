import numpy as np
import matplotlib.pyplot as plt
from itertools import product

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_position('center')
ax.spines['top'].set_position('center')
basis = np.array([[1, 3], [3, -1]])
x, y = [], []

for i, j in product(range(-3, 3), repeat=2):
    v = i * basis[0] + j * basis[1]
    x.append(v[0])
    y.append(v[1])
    draw_circle = plt.Circle((v[0], v[1]), 0.9, fill=False)
    ax.add_artist(draw_circle)

plt.plot(x, y, 'bo')
plt.show()