all:
	g++ -c algebra3.cpp -o algebra3.o
	g++ -c imageIO.cpp -o imageIO.o
	g++ -c ray.cpp -o ray.o
	g++ -c raycast.cpp -o raycast.o
	g++ -c camera.cpp -o camera.o
	# g++ hw1.cpp camera.o raycast.o ray.o imageIO.o algebra3.o -o hw1
	g++ hw2.cpp camera.o raycast.o ray.o imageIO.o algebra3.o -o hw2
	g++ test.cpp camera.o raycast.o ray.o imageIO.o algebra3.o -o test

clear:
	rm *.o