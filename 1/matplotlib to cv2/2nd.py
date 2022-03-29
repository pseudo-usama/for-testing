import matplotlib.pyplot as plt
import cv2
import numpy as np
import matplotlib
from matplotlib.backend_bases import FigureCanvas


fig = plt.figure()
canvas = FigureCanvas(fig)
canvas.draw()

# convert canvas to image
graph_image = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
graph_image  = graph_image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

# it still is rgb, convert to opencv's default bgr
graph_image = cv2.cvtColor(graph_image,cv2.COLOR_RGB2BGR)
