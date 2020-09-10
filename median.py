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

    cdtype = None
    func = None
    if im.dtype == np.float32:
        cdtype = ctypes.c_float
        func = libmedian.median3_filter_float
    if im.dtype == np.float64:
        cdtype = ctypes.c_double
        func = libmedian.median3_filter_double
    if cdtype is None:
        raise Exception("type error")

    filtered = np.ascontiguousarray(np.empty(shape=im.shape, dtype=im.dtype))
    filtered_ptr = filtered.ctypes.data_as(ctypes.POINTER(cdtype))
    im_ptr = im.ctypes.data_as(ctypes.POINTER(cdtype))
    func(filtered_ptr, im_ptr, im.shape[0], im.shape[1])
    return filtered


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

