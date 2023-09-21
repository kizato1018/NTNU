#include "camera.h"
#include "ray.h"
#include "raycast.h"

#include <iostream>
using namespace std;

ColorImage Camera::Render(int width, int height, std::vector<Sphere> spheres, std::vector<Triangle> triangles) {
    ColorImage img;
    // Sphere s(vec3(0.2, 0.2, 1), 0.65);
    // Triangle t1(vec3(-0.5, -0.5, 0.0), vec3(-0.5, -0.5, 1.0), vec3(0.5, -0.5, 1.0));
    // Triangle t2(vec3(-0.5, -0.5, 0.0), vec3(0.5, -0.5, 0.0), vec3(0.5, -0.5, 1.0));
    
    img.init(width, height);
    float dx = (_upper_right - _upper_left).length() / (width-1);
    float dy = (_upper_left - _lower_left).length() / (height-1);
    for(int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            vec3 target = _upper_left + (_lower_left - _upper_left) * dy * y + (_upper_right - _upper_left) * dx * x;
            vec3 direction = target - _position;
            Ray ray(_position, direction);
            vec3 intersection;
            bool hit = false;
            for(auto s : spheres) {
                vec3 inter;
                if(raySphereIntersection(ray, s, inter)) {
                    if(hit)  
                        intersection = (inter.length2() < intersection.length2()) ? inter : intersection;
                    else
                        intersection = inter;
                    hit = true;
                }
            }
            for(auto t : triangles) {
                vec3 inter;
                if(rayTriangleIntersection(ray, t, inter)) {
                    if(hit)
                        intersection = (inter.length2() < intersection.length2()) ? inter : intersection;
                    else
                        intersection = inter;
                    hit = true;
                }
            }
            if(hit) {
                Pixel p;
                p.R = 255 * (intersection[0] + 1.0) / 2.0;
                p.G = 255 * (intersection[1] + 1.0) / 2.0;
                p.B = 255 * (intersection[2] + 1.0) / 2.0;
                img.writePixel(x, y, p);
            }

        }
    }
    return img;
}



// -0.5 0.5 0 
// 0.5 0.5 0
//  -0.5, -0.5, 0
//  0.5, -0.5, 0
// T -0.5, -0.5, 0.0 -0.5, -0.5, 1.0 0.5, -0.5, 1.0
// T -0.5, -0.5, 0.0  0.5, -0.5, 0.0 0.5, -0.5, 1.0