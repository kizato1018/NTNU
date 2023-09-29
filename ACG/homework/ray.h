#ifndef RAY_H
#define RAY_H

#include "algebra3.h"
#include <iostream>

class Ray{
public:
    Ray() {}
    Ray(vec3 origin, vec3 direction) : _origin(origin), _direction(direction.normalize()) {}
    ~Ray() {}
    vec3 origin() const {return _origin;}
    vec3 direction() const {return _direction;}

    std::string ToString();
private:
    vec3 _origin;
    vec3 _direction;
};


#endif