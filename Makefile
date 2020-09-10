CC = g++
CFLAGS =  -std=c++17 -O3 -fPIC -I./

CLEAN = rm -f *.o

lib: obj
	$(CC) $(CFLAGS) -shared -o libmedian3filter.so *.o
	$(CLEAN)
obj:
	$(CC) $(CFLAGS) -c -o median.o median.cc

clean:
	$(CLEAN)

