#ifndef RAY_H
#define RAY_H

#include "algebra3.h"
#include <iostream>

class Ray{
public:
    Ray() {}
    Ray(vec3 origin, vec3 direction) : origin(origin), direction(direction) {}
    ~Ray() {}

    std::string ToString();

    vec3 origin;
    vec3 direction;
};


#endif