# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

from skimage.segmentation import felzenszwalb, mark_boundaries
from skimage import io
from argparse import ArgumentParser

# Importing the arguments
parser = ArgumentParser()
parser.add_argument('--label_id', '-l', type = int)
parser.add_argument('--action', '-a', type = str, choices=['segment', 'view'])
args = parser.parse_args()
label_id = args.label_id
action = args.action

# Importing the image
filename = "r1240_39_satellite_image_spot5_2.5m_gambia_river_gambia_2006.jpg"
img = io.imread(filename)
# img = img[1250: 1500, 250: 500, :]
height, width, _ = img.shape

# Segmenting the image
# segments_fz = felzenszwalb(img, scale=300, sigma=0.5, min_size=10)
# number_of_segments = len(np.unique(segments_fz))

# Computing attribute for each segments
if action == "segment":
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

	data_fieldnames = ["label_id", "avg_red", "avg_green", "avg_blue","total_pixel"]
	with open("labeled_dataset_3.csv", "w") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = data_fieldnames)
		writer.writeheader()
		for i in range (number_of_segments):
			row = {
				"label_id": i,
				"avg_red": objects[i]["total_R"] // objects[i]["total_pixel"],
				"avg_green": objects[i]["total_G"] // objects[i]["total_pixel"],
				"avg_blue": objects[i]["total_B"] // objects[i]["total_pixel"],
				"total_pixel": objects[i]["total_pixel"]
			}
			if objects[i]["total_pixel"] > 1000:
				writer.writerow(row)

# Visualizing image for visual classification
if action == "view":
	fig, ax1 = plt.subplots(figsize=(12, 8))

	# for i in range (height):
	# 	for j in range (width):
	# 		if segments_fz[i][j] != label_id:
	# 			img[i][j][0] = 0
	# 			img[i][j][1] = 0
	# 			img[i][j][2] = 0

	ax1.imshow(img)
	# ax1.imshow(mark_boundaries(img, segments_fz))
	plt.tight_layout()
	plt.show()