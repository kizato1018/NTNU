#include "ray.h"

std::string Ray::ToString() {
    char c_str[128];
    std::sprintf(c_str, "Origin: (%f, %f, %f), Dir: (%f, %f, %f)", origin[0], origin[1], origin[2], direction[0], direction[1], direction[2]);
    return std::string(c_str);
}