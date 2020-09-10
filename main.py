import time

import numpy as np
from scipy import ndimage

from median import median3_filter

im = np.random.random(size= (3, 800, 600)).astype(np.float64)

t0 = time.time()
median3_filter(im)
t1 = time.time()
print(t1-t0)


t0 = time.time()
ndimage.median_filter(im, size= 3)
t1 = time.time()
print(t1-t0)
