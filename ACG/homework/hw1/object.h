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
    inline void setMaterial(float R, float G, float B, float Ka, float Kd, float Ks, float exp, float reflect) {
        _color = vec3(R, G, B);
        _Ka = Ka;
        _Kd = Kd;
        _Ks = Ks;
        _exp = exp;
        _reflect = reflect;
    }
    inline void push_back(const Triangle &triangle) {_triangles.push_back(triangle);}
    inline void push_back(const Sphere &sphere) {_spheres.push_back(sphere);}
    std::vector<Triangle> triangles() const {return _triangles;}
    std::vector<Sphere> spheres() const {return _spheres;} 
    vec3 color() const {return _color;}
    float Ka() const {return _Ka;}
    float Kd() const {return _Kd;}
    float Ks() const {return _Ks;}
    float exp() const {return _exp;}
    float reflect() const {return _reflect;}
    

private:
    vec3 _color;
    float _Ka, _Kd, _Ks, _exp, _reflect;
    std::vector<Triangle> _triangles;
    std::vector<Sphere> _spheres;
};

#endif