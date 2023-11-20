#ifndef LIGHT_H
#define LIGHT_H

#include "algebra3.h"

class Light {
public:
    Light() {}
    Light(vec3 position) : _position(position), _color(1,1,1) {}
    Light(vec3 position, vec3 color) : _position(position), _color(color) {}
    vec3 position() const {return _position;}
    vec3 color() const {return _color;}
private:
    vec3 _position;
    vec3 _color;
};

#endif