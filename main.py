import time

import numpy as np

from median import median3_filter

im = np.random.random(size= (3, 800, 600)).astype(np.float32)

t0 = time.time()
median3_filter(im)
t1 = time.time()
print(t1-t0)