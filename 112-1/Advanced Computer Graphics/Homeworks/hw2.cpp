#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "algebra3.h"
#include "ray.h"
#include "sphere.h"
#include "triangle.h"
#include "object.h"
#include "light.h"
#include "camera.h"
#include "imageIO.h"
using namespace std;

int main() {
    int width = 0;
    int height = 0;
    Camera camera;
    vector<Object> objects;
    vector<Light> lights;
    

    ifstream inputFile("hw2_input.txt");  // Open the input file
    if (!inputFile) {
        cerr << "Error: Unable to open input file." << endl;
        return 1;
    }

    string line;
    double ex, ey, ez;
    double dx, dy, dz, ux, uy, uz;
    double f;
    Object *object = nullptr;
    while (getline(inputFile, line)) {
        istringstream iss(line);
        char type;
        iss >> type;

        if (type == 'E') {
            iss >> ex >> ey >> ez;
            // Create a Camera instance and store it
        } else if (type == 'V') {
            iss >> dx >> dy >> dz >> ux >> uy >> uz;
            // Create an output object or store the values as needed
        } else if (type == 'F') {
            iss >> f;
        } else if (type == 'R') {
            iss >> width >> height;
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
        } else if (type == 'M') {
            double R, G, B, Ka, Kd, Ks, exp, reflect;
            if (object != nullptr)
                objects.push_back(*object);
            object = new Object();
            iss >> R >> G >> B >> Ka >> Kd >> Ks >> exp >> reflect;
            object->setMaterial(R, G, B, Ka, Kd, Ks, exp, reflect);
        } else if (type == 'L') {
            double lx, ly, lz;
            iss >> lx >> ly >> lz;
            lights.push_back(Light(vec3(lx, ly, lz)));
        }
    }
    objects.push_back(*object);
    camera = Camera(vec3(ex, ey, ez), vec3(dx, dy, dz), vec3(ux, uy, uz), f, width, height);
    // Do further processing with the data, such as ray tracing, image generation, etc.
    ColorImage image = camera.Render(objects, lights);
    image.outputPPM("output.ppm");

    inputFile.close();  // Close the input file

    return 0;

}