#ifndef CAMERA_H
#define CAMERA_H
#include <vector>
#include "algebra3.h"
#include "imageIO.h"
#include "ray.h"
#include "sphere.h"
#include "triangle.h"
#include "object.h"
#include "light.h"

class Camera{
public:
    Camera() {}
    Camera(const vec3 position) : _position(position), _background_color(0) {}
    Camera(const vec3 position, vec3 direction, vec3 world_up, float fov, int width, int height);
    Camera(const vec3 position, const vec3 upper_left, const vec3 upper_right, const vec3 lower_left, const vec3 lower_right) : _position(position), _upper_left(upper_left), _upper_right(upper_right), _lower_left(lower_left), _lower_right(lower_right), _background_color(0) {}
    void setPos(const vec3 position) {_position = vec3(position);}
    void setDirection(const vec3 direction) {_direction = vec3(direction);}
    void setUp(const vec3 world_up) {_world_up = vec3(world_up);}
    void setFOV(const float fov) {_fov = fov;}
    void setResolution(int width, int height) {_width = width; _height = height;}
    void setOutpos(const vec3 upper_left, const vec3 upper_right, const vec3 lower_left, const vec3 lower_right) {
        _upper_left = vec3(upper_left);
        _upper_right = vec3(upper_right);
        _lower_left = vec3(lower_left);
        _lower_right = vec3(lower_right);
    }
    vec3 position() const {return _position;}
    vec3 direction() const {return _direction;}
    float fov() const {return _fov;}
    vec3 upper_left() const {return _upper_left;}
    vec3 upper_right() const {return _upper_right;}
    vec3 lower_left() const {return _lower_left;}
    vec3 lower_right() const {return _lower_right;}

    ColorImage Render(const std::vector<Sphere> &spheres, const std::vector<Triangle> &triangles);
    ColorImage Render(const std::vector<Object> &objects);
    ColorImage Render(const std::vector<Object> &objects, const std::vector<Light>& lights);

private:
    vec3 _position;
    vec3 _direction;
    vec3 _world_up;
    float _fov;
    vec3 _upper_left;
    vec3 _upper_right;
    vec3 _lower_left;
    vec3 _lower_right;
    int _width;
    int _height;
    vec3 _background_color;

    // bool _ray_trace(const Ray &ray, const std::vector<Sphere> &spheres, const std::vector<Triangle> &triangles, vec3 &intersection, vec3 &normal_vector);
    // bool _ray_trace(const Ray &ray, const std::vector<Object> &objects, vec3 &intersection);
    // bool _ray_trace(const Ray &ray, const Light &light, const std::vector<Object> &objects, vec3 &intersection, Pixel &pixel);
    // vec3 _phong_model(const Ray &ray, const Light &light, const Object &object, const vec3 &intersection, const vec3 &normal_vector);
};

#endif