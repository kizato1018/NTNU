#include "algebra3.h"
#include "raytrace.h"

void print(char* s, vec3 v) {
    printf(s);
    printf("(%f, %f, %f)\n", v[0], v[1], v[2]);
}

bool rayTriangleIntersection(const Ray& ray, const Triangle& triangle, HitRecord& hitrec) {
    // Möller–Trumbore intersection algorithm
    const double EPS = 1e-6;

    vec3 e1, e2, h, s, q;
    double a, f, u, v;
    vec3 direction = ray.direction().normalize();

    e1 = triangle.v1() - triangle.v0();
    e2 = triangle.v2() - triangle.v0();
    
    h = direction ^ e2;
    a = e1 * h;

    if (std::fabs(a) < EPS)
        return false; // Ray is parallel to the triangle.

    f = 1.0 / a;
    s = ray.origin() - triangle.v0();
    u = f * s * h;

    if (u < 0.0 || u > 1.0)
        return false;

    q = s ^ e1;
    v = f * direction * q;

    if (v < 0.0 || u + v > 1.0)
        return false;

    // At this point, we have a valid intersection.
    double t = f * e2 * q;
    if (t > EPS) {
        vec3 intersection = ray.origin() + direction * t;
        vec3 normal_vector =  (e1 ^ e2).normalize();
        normal_vector = (normal_vector * direction > 0) ? -normal_vector : normal_vector;
        vec3 in_v = intersection - ray.origin();
        vec3 reflect_vector = in_v - 2.0 * (in_v * normal_vector) * normal_vector;
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
    vec3 oc =  ray.origin() - sphere.center();
    vec3 direction = ray.direction().normalize();
    double A = direction * direction;
    double B = 2.0 * oc * direction;
    double C = oc * oc - sphere.radius() * sphere.radius();

    // Calculate the discriminant (D = B^2 - 4AC)
    double discriminant = B * B - 4 * A * C;

    if (discriminant > 0) {
        // Two real roots, ray intersects the sphere
        double t1 = (-B - sqrt(discriminant)) / (2.0 * A);
        double t2 = (-B + sqrt(discriminant)) / (2.0 * A);

        // Choose the closest intersection point (the one with the smallest positive t value)
        double t = (t1 < t2) ? t1 : t2;
        if(t <= 0 ) return false;

        // Calculate the intersection point
        vec3 intersection = ray.origin() + direction * t;
        vec3 normal_vector = (intersection - sphere.center()).normalize();
        vec3 in_v = intersection - ray.origin();
        vec3 reflect_vector = in_v - 2.0 * (in_v * normal_vector) * normal_vector;
        hitrec.in_ray = ray;
        hitrec.normal_vector = normal_vector;
        hitrec.reflect_ray = Ray(intersection, reflect_vector);
        hitrec.length2 = (intersection - ray.origin()).length2();
        return true;
    } else if (discriminant == 0) {
        // One real root, ray grazes the sphere (tangent)
        double t = -B / (2.0 * A);
        if(t <= 0) return false;
        vec3 intersection = ray.origin() + direction * t;
        vec3 normal_vector = (intersection - sphere.center()).normalize();
        vec3 in_v = intersection - ray.origin();
        vec3 reflect_vector = in_v - 2.0 * (in_v * normal_vector) * normal_vector;
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
    for(int i = 0; i < objects.size(); i++) {
        rec.hit_object = &objects[i];
        for(auto s : objects[i].spheres()) {
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
        for(auto t : objects[i].triangles()) {
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
    const double EPS = 1e-4;
    for(auto light : lights) {
        vec3 light_direct = light.position() - intersection;
        // vec3 origin = intersection; //(0.249118, 0.588258, 0.481017)
        vec3 origin = intersection + light_direct * EPS; // (0.296627, 0.632375, 0.426207)
        light_direct = light.position() - intersection;
        Ray ray(origin, light_direct);
        // print("intersection:", intersection);
        // print("shadow ray origin:", origin);
        // print("intersection:", ray.origin());
        // print("shadow ray origin:", ray.direction());

        HitRecord rec;
        for(auto o : objects) {
            for(auto s : o.spheres()) {
                bool hit = raySphereIntersection(ray, s, rec);
                if(hit){
                    // printf("shadow hit sphere\n");
                    // print("shadow intersection:", rec.reflect_ray.origin());
                    return true;
                }
            }
            for(auto t : o.triangles()) {
                bool hit = rayTriangleIntersection(ray, t, rec);
                if(hit){
                    // printf("shadow hit triangle\n");
                    return true;
                }
            }
        }
    }
    return false;
}


vec3 Shade(const Ray& ray, const std::vector<Light>& lights, const std::vector<Object> &objects, const vec3 &background, int depth, int max_depth) {
    const double EPS = 1e-4;
    
    vec3 color = background;
    vec3 I_ambient;
    vec3 I_diffuse;
    vec3 I_specular;
    vec3 I_reflect;
    HitRecord rec;

    // Ray r(ray.origin() + EPS * ray.direction(), ray.direction());
    bool hit = rayTrace(ray, objects, rec);
    bool shadow = false;
    if (hit) {
        const Object& object = *(rec.hit_object);
        I_ambient = object.color()  * object.Ka();
        shadow = inShadow(rec.reflect_ray.origin(), lights, objects);
        if (!shadow) {
            for(auto light : lights) {
                vec3 light_direction = (light.position() - rec.reflect_ray.origin()).normalize();
                float cos_theta = rec.normal_vector * light_direction;
                if(cos_theta > 0)
                    I_diffuse = object.color() * object.Kd() * cos_theta;
                vec3 h_vector = (light_direction - ray.direction().normalize()) * 0.5;
                float cos_alpha = h_vector * rec.normal_vector;
                // float cos_alpha = -ray.direction() * rec.reflect_ray.direction();
                if(cos_alpha > 0)
                    I_specular = light.color() * object.Ks() * pow(cos_alpha, object.exp());
            }
            if(depth < max_depth) {
                // if(object.reflect() > 0) {
                    // printf("Reflect %d\n", depth+1);
                    // print("ray origin:", ray.origin());
                    // print("ray direction:", ray.direction());
                    // print("normal vector", rec.normal_vector);
                    // print("reflect origin:", rec.reflect_ray.origin());
                    // print("reflect direction:", rec.reflect_ray.direction());
                    I_reflect = object.reflect() * Shade(rec.reflect_ray, lights, objects, vec3(0), depth+1, max_depth);
                // }
            }
        }
        // printf("hit object: %s\n", object.name().c_str());
    }
    color = ((1 - rec.hit_object->reflect()) * (I_ambient + I_diffuse + I_specular + I_reflect)) + (rec.hit_object->reflect() * I_reflect);
    color[0] = (color[0] > 1) ? 1 : color[0];
    color[1] = (color[1] > 1) ? 1 : color[1];
    color[2] = (color[2] > 1) ? 1 : color[2];
    // if(shadow) {
    //     printf("In shadow\n");
    // }
    // print("I_ambient:", I_ambient);
    // print("I_diffuse:", I_diffuse);
    // print("I_specular:", I_specular);
    // print("I_reflect:", I_reflect);
    // print("color:", color);
    // puts("");
    return color;
}

