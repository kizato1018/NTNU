#ifndef OBJECT_H
#define OBJECT_H

#include <vector>
#include "algebra3.h"
#include "triangle.h"
#include "sphere.h"


class Object{
public:
    Object() {}
    ~Object() {}
    

private:
    std::vector<Triangle> _triangles;
    std::vector<Sphere> _spheres;
};

#endif