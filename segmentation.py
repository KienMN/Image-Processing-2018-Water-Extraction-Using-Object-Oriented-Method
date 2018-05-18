# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import csv

from skimage.segmentation import felzenszwalb
from skimage.segmentation import mark_boundaries
from skimage import io

# Importing original image
filename = "r1240_39_satellite_image_spot5_2.5m_gambia_river_gambia_2006.jpg"
img = io.imread(filename)
img = img[1250: 1500, 250: 500, :]
height, width, _ = img.shape

# Segmenting image
segments_fz = felzenszwalb(img, scale=300, sigma=0.5, min_size=10)
number_of_segments = len(np.unique(segments_fz))

# Exporting segmentation result
with open ("segments_2.csv", "w") as csvfile:
	writer = csv.writer(csvfile)
	for i in range (height):
		writer.writerow(segments_fz[i])

# Computing attribute of each objects
objects = {}
for i in range (height):
	for j in range (width):
		segment_label = segments_fz[i][j]
		if objects.get(segment_label) is None:
			objects[segment_label] = {}
			objects[segment_label]["total_R"] = img[i][j][0].astype(int)
			objects[segment_label]["total_G"] = img[i][j][1].astype(int)
			objects[segment_label]["total_B"] = img[i][j][2].astype(int)
			objects[segment_label]["total_pixel"] = 1
		else:
			objects[segment_label]["total_R"] += img[i][j][0].astype(int)
			objects[segment_label]["total_G"] += img[i][j][1].astype(int)
			objects[segment_label]["total_B"] += img[i][j][2].astype(int)
			objects[segment_label]["total_pixel"] += 1

# Exporting computation result
data_fieldnames = ["label_id", "avg_red", "avg_green", "avg_blue"]
with open("dataset_2.csv", "w") as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames = data_fieldnames)
	writer.writeheader()
	for i in range (number_of_segments):
		row = {
			"label_id": i,
			"avg_red": objects[i]["total_R"] // objects[i]["total_pixel"],
			"avg_green": objects[i]["total_G"] // objects[i]["total_pixel"],
			"avg_blue": objects[i]["total_B"] // objects[i]["total_pixel"]
		}
		writer.writerow(row)

# Visualizing the traing set results
fig, ax = plt.subplots(figsize=(12, 8))
ax.imshow(mark_boundaries(img, segments_fz))
ax.set_title("Segmentation")
plt.tight_layout()
plt.show()