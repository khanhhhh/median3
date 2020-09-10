template<typename type>
inline void swap_sort(type& a, type& b) {
	if (a > b) {
		type temp = a;
		a = b;
		b = temp;
	}
}
#include<array>
// source: http://ndevilla.free.fr/median/median.pdf
template<typename dtype>
inline dtype median9(std::array<dtype, 9> arr) {
	swap_sort(arr[1], arr[2]);
	swap_sort(arr[4], arr[5]);
	swap_sort(arr[7], arr[8]);
	swap_sort(arr[0], arr[1]);
	swap_sort(arr[3], arr[4]);
	swap_sort(arr[6], arr[7]);
	swap_sort(arr[1], arr[2]);
	swap_sort(arr[4], arr[5]);
	swap_sort(arr[7], arr[8]);
	swap_sort(arr[0], arr[3]);
	swap_sort(arr[5], arr[8]);
	swap_sort(arr[4], arr[7]);
	swap_sort(arr[3], arr[6]);
	swap_sort(arr[1], arr[4]);
	swap_sort(arr[2], arr[5]);
	swap_sort(arr[4], arr[7]);
	swap_sort(arr[4], arr[2]);
	swap_sort(arr[6], arr[4]);
	swap_sort(arr[4], arr[2]);
	return arr[4];
}
template<typename dtype, typename itype>
void median3_filter(dtype* dst, const dtype* src, itype height, itype width) {
	for (itype h=0; h<height; h++)
	for (itype w=0; w<width; w++) {
		if (h == 0 or h == height-1 or w == 0 or w == width-1)
			dst[h*width+w] = src[h*width+w];
		else {
			std::array<dtype, 9> arr = {
				src[h*width+w],
				src[h*width+w+1],
				src[h*width+w-1],
				src[(h+1)*width+w],
				src[(h-1)*width+w],
				src[(h+1)*width+w+1],
				src[(h+1)*width+w-1],
				src[(h-1)*width+w+1],
				src[(h-1)*width+w-1],
			};
			dst[h*width+w] = median9(arr);
		}
	}
}
#include"median.h"
extern "C" {
void median3_filter_float(float* dst, const float* src, int64_t height, int64_t width) {
	median3_filter<float, int64_t>(dst, src, height, width);
}
void median3_filter_double(double* dst, const double* src, int64_t height, int64_t width) {
	median3_filter<double, int64_t>(dst, src, height, width);
}
}



