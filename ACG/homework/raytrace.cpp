#include "algebra3.h"
#include "raytrace.h"

bool rayTriangleIntersection(const Ray& ray, const Triangle& triangle, HitRecord& hitrec) {
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
        vec3 intersection = ray.origin() + ray.direction() * t;
        vec3 normal_vector =  (e1 ^ e2).normalize();
        normal_vector = (normal_vector * ray.direction() > 0) ? -normal_vector : normal_vector;
        vec3 reflect_vector = intersection + ray.direction() + 2 * hitrec.normal_vector;
        hitrec.in_ray = ray;
        hitrec.normal_vector = normal_vector;
        hitrec.reflect_ray = Ray(intersection, reflect_vector);
        hitrec.length2 = (intersection - ray.origin()).length2();
        return true;
    }

    return false;
}

bool raySphereIntersection(const Ray& ray, const Sphere& sphere, HitRecord& hitrec) {
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
        vec3 intersection = ray.origin() + ray.direction() * t;
        vec3 normal_vector = (intersection - sphere.center()).normalize();
        vec3 reflect_vector = intersection + ray.direction() + 2 * hitrec.normal_vector;
        hitrec.in_ray = ray;
        hitrec.normal_vector = normal_vector;
        hitrec.reflect_ray = Ray(intersection, reflect_vector);
        hitrec.length2 = (intersection - ray.origin()).length2();
        return true;
    } else if (discriminant == 0) {
        // One real root, ray grazes the sphere (tangent)
        double t = -B / (2.0 * A);
        vec3 intersection = ray.origin() + ray.direction() * t;
        vec3 normal_vector = (intersection - sphere.center()).normalize();
        vec3 reflect_vector = intersection + ray.direction() + 2 * hitrec.normal_vector;
        hitrec.in_ray = ray;
        hitrec.normal_vector = normal_vector;
        hitrec.reflect_ray = Ray(intersection, reflect_vector);
        hitrec.length2 = (intersection - ray.origin()).length2();
        return true;
    } else {
        // No real roots, ray misses the sphere
        return false;
    }
}

bool rayTrace(const Ray& ray, const std::vector<Object> &objects, HitRecord& hitrec) {
    bool ishit = false;
    HitRecord rec;
    for(auto o : objects) {
        rec.hit_object = &o;
        for(auto s : o.spheres()) {
            bool hit = raySphereIntersection(ray, s, rec);
            if(hit){
                if(!ishit){
                    hitrec = rec;
                    ishit = true;
                }
                else if(rec.length2 < hitrec.length2) {
                    hitrec = rec;
                }
            }
        }
        for(auto t : o.triangles()) {
            bool hit = rayTriangleIntersection(ray, t, rec);
            if(hit){
                if(!ishit){
                    hitrec = rec;
                    ishit = true;
                }
                else if(rec.length2 < hitrec.length2) {
                    hitrec = rec;
                }
            }
        }
    }
    return ishit;
}

bool inShadow(const vec3& intersection, const std::vector<Light>& lights, const std::vector<Object> &objects) {
    // bool inshadow = false;
    for(auto light : lights) {
        Ray ray(intersection, light.position() - intersection);
        HitRecord rec;
        for(auto o : objects) {
            for(auto s : o.spheres()) {
                bool hit = raySphereIntersection(ray, s, rec);
                if(hit){
                    return true;
                }
            }
            for(auto t : o.triangles()) {
                bool hit = rayTriangleIntersection(ray, t, rec);
                if(hit){
                    return true;
                }
            }
        }
    }
}

vec3 Shade(const Ray& ray, const std::vector<Light>& lights, const std::vector<Object> &objects, const vec3 &background, int depth, int max_depth) {
    vec3 color = background;

    HitRecord rec;
    bool hit = rayTrace(ray, objects, rec);
    if (hit) {
        Object& object = *rec.hit_object;
        color = object.color()  * object.Ka();
        bool shadow = inShadow(rec.reflect_ray.origin(), lights, objects);
        if (!shadow) {
            for(auto light : lights) {
                vec3 light_direction = (light.position() - rec.reflect_ray.origin()).normalize();
                float cos_theta = rec.normal_vector * light_direction;
                if(cos_theta > 0)
                    color += light.color() * object.color() * object.Kd() * cos_theta;
                float cos_alpha = -ray.direction() * rec.reflect_ray.direction();
                if(cos_alpha > 0)
                    color += light.color() * object.Ks() * pow(cos_alpha, object.exp());
            }
            if(depth < max_depth) {
                if(object.reflect() > 0) {
                    color += object.reflect() * Shade(rec.reflect_ray, lights, objects, vec3(0), depth+1);
                }
            }
        }
    }
}
