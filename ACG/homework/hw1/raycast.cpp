#include "algebra3.h"
#include "raycast.h"

bool rayTriangleIntersection(const Ray& ray, const Triangle& triangle, vec3& intersectionPoint) {
    // Möller–Trumbore intersection algorithm
    const double EPS = 1e-6;

    vec3 e1, e2, h, s, q;
    double a, f, u, v;

    e1 = triangle.v1() - triangle.v0();
    e2 = triangle.v2() - triangle.v0();
    
    h = ray.direction() ^ e2;
    a = e1 * h;

    if (std::fabs(a) < EPS)
        return false; // Ray is parallel to the triangle.

    f = 1.0 / a;
    s = ray.origin() - triangle.v0();
    u = f * s * h;

    if (u < 0.0 || u > 1.0)
        return false;

    q = s ^ e1;
    v = f * ray.direction() * q;

    if (v < 0.0 || u + v > 1.0)
        return false;

    // At this point, we have a valid intersection.
    double t = f * e2 * q;
    if (t > EPS) {
        intersectionPoint = ray.origin() + ray.direction() * t;
        return true;
    }

    return false;
}

bool raySphereIntersection(const Ray& ray, const Sphere& sphere, vec3& intersectionPoint) {
    // Calculate the coefficients for the quadratic equation (At^2 + Bt + C = 0)
    vec3 oc = ray.origin() - sphere.center();
    double A = ray.direction() * ray.direction();
    double B = 2.0 * oc * ray.direction();
    double C = oc * oc - sphere.radius() * sphere.radius();

    // Calculate the discriminant (D = B^2 - 4AC)
    double discriminant = B * B - 4 * A * C;

    if (discriminant > 0) {
        // Two real roots, ray intersects the sphere
        double t1 = (-B - sqrt(discriminant)) / (2.0 * A);
        double t2 = (-B + sqrt(discriminant)) / (2.0 * A);

        // Choose the closest intersection point (the one with the smallest positive t value)
        double t = (t1 < t2) ? t1 : t2;

        // Calculate the intersection point
        intersectionPoint = ray.origin() + ray.direction() * t;
        return true;
    } else if (discriminant == 0) {
        // One real root, ray grazes the sphere (tangent)
        double t = -B / (2.0 * A);
        intersectionPoint = ray.origin() + ray.direction() * t;
        return true;
    } else {
        // No real roots, ray misses the sphere
        return false;
    }
}
