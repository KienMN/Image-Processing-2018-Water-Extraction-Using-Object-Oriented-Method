import numpy as np

def findMaxIntensity(S):
	np.array(S)
	return np.max(S)

def findMinIntensity(S):
	np.array(S)
	return np.min(S)

def findMedianIntensity(S):
	np.array(S)
	return np.median(S)

def adaptiveMedianFilter(I, maxSize):
	I = np.array(I)
	# Initializing parameters
	max_size_x, max_size_y = maxSize
	if (max_size_x % 2 == 0 or max_size_y % 2 == 0):
		print("max size must be odd number")
		return
	m, n = I.shape
	int_size_x, int_size_y = (3, 3)

	# Creating new matrix with zeros in border
	new_I = np.zeros(m + max_size_y - 1, n + max_size_x - 1)
	new_I[(max_size_y - 1) // 2: (max_size_y - 1) // 2 + m, (max_size_x - 1) // 2: (max_size_x - 1) // 2 + n] = I
	
	# Filtering
	for j in range ((max_size_y - 1) // 2, (max_size_y - 1) // 2 + m):
		for i in range ((max_size_x - 1) // 2, (max_size_x - 1) // 2 + n):
			current_size_x, current_size_y = (int_size_x, int_size_y)
			z_xy = new_I[j, i]
			while current_size_x <= max_size_x and current_size_y <= max_size_y:
				S = new_I[j - (current_size_y - 1) // 2: j - (current_size_y - 1) // 2 + current_size_y, i - (current_size_x - 1) // 2: i - (current_size_x - 1) // 2 + current_size_x]
				z_min = findMinIntensity(S)
				z_max = findMaxIntensity(S)
				z_med = findMedianIntensity(S)
				A1 = z_med - z_min
				A2 = z_med - z_max
				if (A1 > 0 and A2 < 0):
					B1 = z_xy - z_min
					B2 = z_xy - z_max
					if B1 > 0 and B2 < 0:
						I[j - (max_size_y - 1) // 2, i - (max_size_x - 1) // 2] = z_xy
					else:
						I[j - (max_size_y - 1) // 2, i - (max_size_x - 1) // 2] = z_med
					break
				current_size_x += 2
				current_size_y += 2
				I[j - (max_size_y - 1) // 2, i - (max_size_x - 1) // 2] = z_xy
	return I