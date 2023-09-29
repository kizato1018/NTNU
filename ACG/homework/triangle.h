#ifndef TRIANGLE_H
#define TRIANGLE_H
#include "algebra3.h"
#include <vector>

class Triangle{
public:
    Triangle();
    Triangle(const vec3 v0, const vec3 v1, const vec3 v2) : _v0(v0), _v1(v1), _v2(v2) {}
    void setV(const vec3 v0, const vec3 v1, const vec3 v2);
    std::vector<vec3> getV();
    vec3 v0() const {return _v0;}
    vec3 v1() const {return _v1;}
    vec3 v2() const {return _v2;}


private:
    vec3 _v0;
    vec3 _v1;
    vec3 _v2;
};

#endif