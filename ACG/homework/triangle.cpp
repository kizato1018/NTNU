#include "triangle.h"

std::vector<vec3> Triangle::getV() {
    std::vector<vec3> v;
    v.push_back(vec3(_v0));
    v.push_back(vec3(_v1));
    v.push_back(vec3(_v2));
    return v;
}

void Triangle::setV(const vec3 v0, const vec3 v1, const vec3 v2) {
    _v0 = vec3(v0);
    _v1 = vec3(v1);
    _v2 = vec3(v2);
}

