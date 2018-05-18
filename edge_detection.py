import numpy as np
import matplotlib.pyplot as plt

from scipy import ndimage as ndi
from skimage import io
from skimage import feature

filename = "r1240_39_satellite_image_spot5_2.5m_gambia_river_gambia_2006.jpg"

image = io.imread(filename, as_grey=True)

print(image.size)

edges = feature.canny(image, sigma = 3)

fill_segment = ndi.binary_fill_holes(edges)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(12, 8))

ax1.imshow(io.imread(filename))
ax1.axis('off')
ax1.set_title('Original image', fontsize=20)

ax2.imshow(edges, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Canny filter, $\sigma=1$', fontsize=20)

ax3.imshow(fill_segment, cmap=plt.cm.gray, interpolation='nearest')
ax3.set_title('Segmentation', fontsize=20)
ax3.axis('off')

plt.show()
# plt.savefig("/Users/kienmaingoc/Desktop/test")

# from skimage import morphology

# segment_cleaned = morphology.remove_small_objects(fill_segment, 21)

# fig, ax = plt.subplots(figsize=(4, 3))
# ax.imshow(segment_cleaned, cmap=plt.cm.gray, interpolation='nearest')
# ax.set_title('removing small objects')
# ax.axis('off')
# plt.show()