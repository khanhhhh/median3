import ctypes
import numpy as np

libmedian = ctypes.cdll.LoadLibrary("./libmedian3filter.so")

mapping = {
    "float32": (np.float32, ctypes.c_float, libmedian.median3_filter_float),
    "float64": (np.float64, ctypes.c_double, libmedian.median3_filter_double),
}

def median3_filter_1channel(im: np.ndarray) -> np.ndarray:
    # checking
    if len(im.shape) != 2:
        raise Exception("shape error")
    if not im.flags.c_contiguous:
        im = np.ascontiguousarray(im)
    # end checking

    cdtype = None
    func = None
    for npt, ct, f in mapping.values():
        if npt == im.dtype:
            cdtype = ct
            func = f

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

