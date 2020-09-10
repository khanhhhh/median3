#ifndef _MEDIAN_H_
#define _MEDIAN_H_
#ifdef __cplusplus
extern "C" {
#include<cstdint>
#else
#include<stdint.h>
#endif
void median3_filter_float(float* dst, const float* src, int64_t height, int64_t width);
#ifdef __cplusplus
}
#endif
#endif
