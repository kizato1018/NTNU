#ifndef LIGHT_H
#define LIGHT_H

#include "algebra3.h"

class Light {
public:
    Light() {}
    Light(vec3 position) : _position(position) {}
    vec3 position() const {return _position;}
private:
    vec3 _position;
};

#endif