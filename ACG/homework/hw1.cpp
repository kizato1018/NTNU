#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "algebra3.h"
#include "ray.h"
#include "sphere.h"
#include "triangle.h"
#include "object.h"
#include "camera.h"
#include "imageIO.h"
using namespace std;

int main() {
    int width = 0;
    int height = 0;
    Camera camera;
    vector<Object> objects;
    Object *object = new Object();

    ifstream inputFile("hw1_input.txt");  // Open the input file
    if (!inputFile) {
        cerr << "Error: Unable to open input file." << endl;
        return 1;
    }

    string line;
    while (getline(inputFile, line)) {
        istringstream iss(line);
        char type;
        iss >> type;

        if (type == 'E') {
            double ex, ey, ez;
            iss >> ex >> ey >> ez;
            // Create a Camera instance and store it
            camera = Camera(vec3(ex, ey, ez));
        } else if (type == 'O') {
            double ulx, uly, ulz, urx, ury, urz, llx, lly, llz, lrx, lry, lrz;
            iss >> ulx >> uly >> ulz >> urx >> ury >> urz >> llx >> lly >> llz >> lrx >> lry >> lrz;
            camera.setOutpos(vec3(ulx, uly, ulz), vec3(urx, ury, urz), vec3(llx, lly, llz), vec3(lrx, lry, lrz));
            // Create an output object or store the values as needed
        } else if (type == 'R') {
            iss >> width >> height;
            camera.setResolution(width, height);
            // Create a resolution object or store the values as needed
        } else if (type == 'S') {
            double sx, sy, sz, sradius;
            iss >> sx >> sy >> sz >> sradius;
            // Create a Sphere instance and store it
            Sphere sphere(vec3(sx, sy, sz), sradius);
            object->push_back(sphere);
        } else if (type == 'T') {
            double v1x, v1y, v1z, v2x, v2y, v2z, v3x, v3y, v3z;
            iss >> v1x >> v1y >> v1z >> v2x >> v2y >> v2z >> v3x >> v3y >> v3z;
            // Create a Triangle instance and store it
            Triangle triangle(vec3(v1x, v1y, v1z), vec3(v2x, v2y, v2z), vec3(v3x, v3y, v3z));
            object->push_back(triangle);
        }
    }
    objects.push_back(*object);

    // Do further processing with the data, such as ray tracing, image generation, etc.
    ColorImage image = camera.Render(objects);
    image.outputPPM("output.ppm");

    inputFile.close();  // Close the input file

    return 0;

}