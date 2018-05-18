# Kernel SVM

# Importing libraries
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

from skimage import io
from skimage.segmentation import felzenszwalb, mark_boundaries

# Importing the dataset
train_dataset = pd.read_csv('labeled_dataset_2.csv')
X_train = train_dataset.iloc[:, 1: 4].values
y_train = train_dataset.iloc[:, 4].values
test_dataset = pd.read_csv('dataset_2.csv')
X_test = test_dataset.iloc[:, 1: 4].values

# Encoding categorical variables
from sklearn.preprocessing import LabelEncoder
label_encoder_y = LabelEncoder()
y_train = label_encoder_y.fit_transform(y_train)
# print(y_train)

# Features scaling
# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)

# Fitting the SVM to the training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the test set results
y_pred = classifier.predict(X_test)

# Visualizing the traing set results
filename = "r1240_39_satellite_image_spot5_2.5m_gambia_river_gambia_2006.jpg"
original_img = io.imread(filename)
original_img = original_img[1250: 1500, 250: 500, :]
img = io.imread(filename)
img = img[1250: 1500, 250: 500, :]
height, width, _ = img.shape

segment_label = pd.read_csv("segments_2.csv", header = None).values

# Object detection
for i in range (height):
	for j in range (width):
		# Grass
		# if y_pred[segment_label[i][j]] == 0:
		# 	img[i][j][0] = 0
		# 	img[i][j][1] = 225
		# 	img[i][j][2] = 0
		# River
		if y_pred[segment_label[i][j]] == 1:
			img[i][j][0] = 0
			img[i][j][1] = 0
			img[i][j][2] = 225
		# Sand
		# elif y_pred[segment_label[i][j]] == 2:
		# 	img[i][j][0] = 225
		# 	img[i][j][1] = 0
		# 	img[i][j][2] = 0
		# White sand
		# elif y_pred[segment_label[i][j]] == 3:
		# 	img[i][j][0] = 225
		# 	img[i][j][1] = 225
		# 	img[i][j][2] = 225
		# Wood
		# elif y_pred[segment_label[i][j]] == 4:
		# 	img[i][j][0] = 0
		# 	img[i][j][1] = 100
		# 	img[i][j][2] = 100

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize=(12, 8))
ax1.imshow(mark_boundaries(original_img, segment_label))
ax1.set_title("Segmentation")
ax2.imshow(img)
ax2.set_title("Water extraction")
# ax1.axis("off")
plt.tight_layout()
plt.show()

