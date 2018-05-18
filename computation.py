# Importing libraries
from skimage import io
import numpy as np
import pandas as pd
import csv

# Importing original image
filename = "r1240_39_satellite_image_spot5_2.5m_gambia_river_gambia_2006.jpg"
img = io.imread(filename)
img = img[1250: 1500, 250: 500, :]
height, width, _ = img.shape

# Getting segments
segments_fz = pd.read_csv("segments_2.csv", header = None).values
number_of_segments = len(np.unique(segments_fz))

# Computing attributes for each objects
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