all:
	g++ -c algebra3.cpp -o algebra3.o
	g++ -c imageIO.cpp -o imageIO.o
	g++ -c ray.cpp -o ray.o
	g++ -c raytrace.cpp -o raytrace.o
	g++ -c camera.cpp -o camera.o
	g++ hw1.cpp camera.o raytrace.o ray.o imageIO.o algebra3.o -o hw1
	g++ hw2.cpp camera.o raytrace.o ray.o imageIO.o algebra3.o -o hw2
	g++ hw3.cpp camera.o raytrace.o ray.o imageIO.o algebra3.o -o hw3
	g++ test.cpp camera.o raytrace.o ray.o imageIO.o algebra3.o -o test

clear:
	rm *.o