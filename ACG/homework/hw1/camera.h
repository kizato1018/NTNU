#ifndef CAMERA_H
#define CAMERA_H
#include <vector>
#include "algebra3.h"
#include "imageIO.h"
#include "sphere.h"
#include "triangle.h"

class Camera{
public:
    Camera() {}
    Camera(const vec3 position) : _position(position) {}
    Camera(const vec3 position, vec3 direction, vec3 world_up, float fov) : _position(position), _direction(direction), _world_up(world_up), _fov(fov) {}
    Camera(const vec3 position, const vec3 upper_left, const vec3 upper_right, const vec3 lower_left, const vec3 lower_right) : _position(position), _upper_left(upper_left), _upper_right(upper_right), _lower_left(lower_left), _lower_right(lower_right) {}
    void setPos(const vec3 position) {_position = vec3(position);}
    void setDirection(const vec3 direction) {_direction = vec3(direction);}
    void setFOV(const float fov) {_fov = fov;}
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

    ColorImage Render(int widht, int height, std::vector<Sphere> spheres, std::vector<Triangle> triangles);
private:
    vec3 _position;
    vec3 _direction;
    vec3 _world_up;
    float _fov;
    vec3 _upper_left;
    vec3 _upper_right;
    vec3 _lower_left;
    vec3 _lower_right;
};

#endif