#ifndef SPHERE_H
#define SPHERE_H
#include "algebra3.h"

class Sphere {
public:
    Sphere();
    Sphere(const vec3 center, const float radius) : _center(center), _radius(radius) {} 
    void set(const vec3 center, const float radius) {_center = vec3(center); _radius = radius;}
    void setCenter(const vec3 center) {_center = vec3(center);}
    void setRadius(const float radius) {_radius = radius;}
    vec3 center() const {return vec3(_center);}
    float radius() const {return _radius;}
private:
    vec3 _center;
    float _radius;
};

#endif