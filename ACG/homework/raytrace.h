#ifndef RAYTRACE_H
#define RAYTRACE_H
#include "algebra3.h"
#include "ray.h"
#include "triangle.h"
#include "sphere.h"
#include "object.h"
#include "light.h"

struct HitRecord{
    HitRecord& operator = (const HitRecord& rec){
        in_ray = rec.in_ray;
        reflect_ray = rec.reflect_ray;
        normal_vector = rec.normal_vector;
        length2 = rec.length2;
        hit_object = rec.hit_object;
        return *this;
    }
    Ray in_ray;
    Ray reflect_ray;
    vec3 normal_vector;
    float length2;
    const Object* hit_object;
};

bool rayTriangleIntersection(const Ray& ray, const Triangle& triangle, HitRecord& hitrec);
bool raySphereIntersection(const Ray& ray, const Sphere& sphere, HitRecord& hitrec);
bool rayTrace(const Ray& ray, const std::vector<Object> &objects, HitRecord& hitrec);
vec3 Shade(const Ray& ray, const std::vector<Light>& lights, const std::vector<Object> &objects, const vec3 &background, int depth=0, int max_depth=10);


#endif