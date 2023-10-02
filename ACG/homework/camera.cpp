#include "algebra3.h"
#include "camera.h"
#include "ray.h"
#include "raytrace.h"


#include <iostream>
using namespace std;

Camera::Camera(const vec3 position, vec3 direction, vec3 world_up, float fov, int width, int height) : _position(position), _direction(direction), _world_up(world_up), _fov(fov), _width(width), _height(height), _background_color(0) {
    double aspect_ratio = static_cast<double>(_height) / static_cast<double>(_width);
    double half_width = tan(_fov * 0.5 * (M_PI / 180.0));
    double half_height = aspect_ratio * half_width;
    // Calculate the center of the image plane (near plane)
    vec3 forward = _direction.normalize();
    vec3 up = _world_up.normalize();
    vec3 right = (up ^ forward).normalize();
    vec3 center = _position + forward;

    // Calculate the four corners
    _upper_left = center - half_width * right + half_height * up;
    _upper_right = center + half_width * right + half_height * up;
    _lower_left = center - half_width * right - half_height * up;
    _lower_right = center + half_width * right - half_height * up;
    printf("upper left:(%f, %f, %f)\n", _upper_left[0], _upper_left[1], _upper_left[2]);
    printf("upper right:(%f, %f, %f)\n", _upper_right[0], _upper_right[1], _upper_right[2]);
    printf("lower left:(%f, %f, %f)\n", _lower_left[0], _lower_left[1], _lower_left[2]);
    printf("lower right:(%f, %f, %f)\n", _lower_right[0], _lower_right[1], _lower_right[2]);
}

ColorImage Camera::Render(const std::vector<Object> &objects) {
    ColorImage img;

    img.init(_width, _height);
    float dx = (_upper_right - _upper_left).length() / (_width-1);
    float dy = (_upper_left - _lower_left).length() / (_height-1);
    for(int y = 0; y < _height; y++) {
        for (int x = 0; x < _width; x++) {
            vec3 target = _upper_left + (_lower_left - _upper_left) * dy * y + (_upper_right - _upper_left) * dx * x;
            vec3 direction = target - _position;
            Ray ray(_position, direction);
            HitRecord rec;
            bool hit = rayTrace(ray, objects, rec);
            
            if(hit) {
                Pixel p;
                p.R = 255 * (rec.reflect_ray.origin()[0] + 1.0) / 2.0;
                p.G = 255 * (rec.reflect_ray.origin()[1] + 1.0) / 2.0;
                p.B = 255 * (rec.reflect_ray.origin()[2] + 1.0) / 2.0;
                img.writePixel(x, y, p);
            }

        }
    }
    return img;
}

ColorImage Camera::Render(const std::vector<Object> &objects, const std::vector<Light>& lights) {
    ColorImage img;
    
    img.init(_width, _height);
    float dx = (_upper_right - _upper_left).length() / (_width-1);
    float dy = (_upper_left - _lower_left).length() / (_height-1);
    for(int y = 0; y < _height; y++) {
        for (int x = 0; x < _width; x++) {
            vec3 target = _upper_left + (_lower_left - _upper_left) * dy * y + (_upper_right - _upper_left) * dx * x;
            vec3 direction = target - _position;
            Ray ray(_position, direction);
            // printf("pos:(%d, %d)\n", x, y);
            vec3 color = Shade(ray, lights, objects, _background_color, 0, 10);
            Pixel p;
            p.R = color[0] * 255;
            p.G = color[1] * 255;
            p.B = color[2] * 255;
            
            img.writePixel(x, y, p);

        }
    }
    return img;
}

// bool Camera::_ray_trace(const Ray &ray, const std::vector<Sphere> &spheres, const std::vector<Triangle> &triangles, vec3 &intersection, vec3 &normal_vector)
// {
//     bool hit = false;
//     for (auto s : spheres)
//     {
//         vec3 inter;
//         if (raySphereIntersection(ray, s, inter))
//         {
//             if ((!hit) || (hit && inter.length2() < intersection.length2())) {
//                 intersection = inter;
//                 normal_vector = intersection - s.center();
//             }
//             hit = true;
//         }
//     }
//     for (auto t : triangles)
//     {
//         vec3 inter;
//         if (rayTriangleIntersection(ray, t, inter))
//         {
//             if ((!hit) || (hit && inter.length2() < intersection.length2())) {
//                 intersection = inter;
//                 vec3 e1, e2;
//                 e1 = t.v1() - t.v0();
//                 e2 = t.v2() - t.v0();
//                 normal_vector = (e1 ^ e2).normalize();
//                 normal_vector = (normal_vector * ray.direction() > 0) ? -normal_vector : normal_vector;
//             }
//             hit = true;
//         }
//     }
//     return hit;
// }

// bool Camera::_ray_trace(const Ray &ray, const std::vector<Object> &objects, vec3 &intersection) {
//     bool hit = false;
//     vec3 normal_vector;
//     for(auto o : objects) {
//         hit |= _ray_trace(ray, o.spheres(), o.triangles(), intersection, normal_vector);
//     }
//     return hit;
// }
// bool Camera::_ray_trace(const Ray &ray, const Light &light, const std::vector<Object> &objects, vec3 &intersection, Pixel &pixel) {
//     bool hit = false;
//     vec3 inter = intersection;
//     vec3 normal_vector;
//     vec3 final_color;
//     for(auto o : objects) {
//         hit |= _ray_trace(ray, o.spheres(), o.triangles(), intersection, normal_vector);
//         if(hit && inter != intersection) {
//             inter = intersection;
//             final_color = _phong_model(ray, light, o, intersection, normal_vector);
//             pixel.R = final_color[0] * 256 - 1;
//             pixel.G = final_color[1] * 256 - 1;
//             pixel.B = final_color[2] * 256 - 1;
//         }
//     }
//     return hit;
// }

// vec3 Camera::_phong_model(const Ray &ray, const Light &light, const Object &object, const vec3 &intersection, const vec3 &normal_vector) {
//     vec3 I_ambient = object.color() * object.Ka();
//     vec3 I_diffuse;
//     vec3 I_specular;
//     vec3 light_direction = (light.position() - intersection).normalize();
//     float cos_theta = normal_vector * light_direction;
//     if(cos_theta > 0)
//         I_diffuse = object.color() * object.Kd() * cos_theta;
//     vec3 h_vector = (light_direction - ray.direction()) * 0.5;
//     float cos_alpha = h_vector * normal_vector;
//     if(cos_alpha > 0)
//         I_specular = object.Ks() * pow(cos_alpha, object.exp());


//     // printf("I_ambient:(%f, %f, %f)\n", I_ambient[0], I_ambient[1], I_ambient[2]);
//     // printf("I_diffuse:(%f, %f, %f)\n", I_diffuse[0], I_diffuse[1], I_diffuse[2]);
//     // printf("I_specular:(%f, %f, %f)\n", I_specular[0], I_specular[1], I_specular[2]);
//     return I_ambient + I_diffuse + I_specular;

// }

// -0.5 0.5 0 
// 0.5 0.5 0
//  -0.5, -0.5, 0
//  0.5, -0.5, 0
// T -0.5, -0.5, 0.0 -0.5, -0.5, 1.0 0.5, -0.5, 1.0
// T -0.5, -0.5, 0.0  0.5, -0.5, 0.0 0.5, -0.5, 1.0