import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.array([1,2,3,4,5])
y = x**2
ax.plot(x, y)

# plt.show()

fig.canvas.draw()
rgba_buf = fig.canvas.buffer_rgba()
(w, h) = fig.canvas.get_width_height()
rgba_arr = np.frombuffer(rgba_buf, dtype=np.uint8).reshape((h, w, 4))

plt.imshow(rgba_arr)
plt.show()

# print(rgba_arr)
