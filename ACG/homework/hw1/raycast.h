#ifndef RAYCAST_H
#define RAYCAST_H
#include "algebra3.h"
#include "ray.h"
#include "triangle.h"
#include "sphere.h"


bool rayTriangleIntersection(const Ray& ray, const Triangle& triangle, vec3& intersectionPoint);
bool raySphereIntersection(const Ray& ray, const Sphere& sphere, vec3& intersectionPoint);
bool raycast();
#endif