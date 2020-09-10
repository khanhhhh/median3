import ctypes
import numpy as np

libmedian = ctypes.cdll.LoadLibrary("./libmedian3filter.so")

def median3_filter_1channel(im: np.ndarray) -> np.ndarray:
    # checking
    if len(im.shape) != 2:
        raise Exception("shape error")
    if not im.flags.c_contiguous:
        im = np.ascontiguousarray(im)
    # end checking

    filtered = np.ascontiguousarray(np.empty(shape=im.shape, dtype=im.dtype))
    if im.dtype == np.float32:
        filtered_ptr = filtered.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        im_ptr = im.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        libmedian.median3_filter_float(filtered_ptr, im_ptr, im.shape[0], im.shape[1])
        return filtered

    raise Exception("type error")

def median3_filter(im: np.ndarray) -> np.ndarray:
    # checking
    if len(im.shape) == 2:
        return median3_filter_1channel(im)
    if len(im.shape) == 3:
        filtered = []
        for ch in im:
            filtered.append(median3_filter_1channel(ch))
        return np.array(filtered)
    #end ehcking
    raise Exception("shape error")

