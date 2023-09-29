#include "ray.h"

std::string Ray::ToString() {
    char c_str[128];
    std::sprintf(c_str, "Origin: (%f, %f, %f), Dir: (%f, %f, %f)", _origin[0], _origin[1], _origin[2], _direction[0], _direction[1], _direction[2]);
    return std::string(c_str);
}