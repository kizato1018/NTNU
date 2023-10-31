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
            vec3 target = _upper_left + (_lower_left - _upper_left).normalize()  * dy * y + (_upper_right - _upper_left).normalize()  * dx * x;
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

// ColorImage Camera::Render(const std::vector<Object> &objects, const std::vector<Light>& lights) {
//     ColorImage img;
    
//     img.init(_width, _height);
//     float dx = (_upper_right - _upper_left).length() / (_width-1);
//     float dy = (_upper_left - _lower_left).length() / (_height-1);
//     for(int y = 0; y < _height; y++) {
//         for (int x = 0; x < _width; x++) {
//             vec3 target = _upper_left + (_lower_left - _upper_left).normalize() * dy * y + (_upper_right - _upper_left).normalize() * dx * x;
//             vec3 direction = target - _position;
//             Ray ray(_position, direction);
//             // printf("pos:(%d, %d)\n", x, y);
//             vec3 color = Shade(ray, lights, objects, _background_color, 0, 10);
//             Pixel p;
//             p.R = color[0] * 255;
//             p.G = color[1] * 255;
//             p.B = color[2] * 255;
            
//             img.writePixel(x, y, p);

//         }
//     }
//     return img;
// }

ColorImage Camera::Render(const std::vector<Object>& objects, const std::vector<Light>& lights) {
    ColorImage img;
    _background_color = vec3(50);

    img.init(_width, _height);
    float dx = (_upper_right - _upper_left).length() / (_width - 1);
    float dy = (_upper_left - _lower_left).length() / (_height - 1);

    float sensor_width = 4.0 / 3.0;  // 4/3 inch format
    float f = 1.50;        // Focal length in meters (15 mm)

    // Calculate the size of the aperture based on the f-number (f/2.2)
    float aperture_radius = f / (2.2 * 2.0);

    // Calculate the distance to the focal plane (in focus)
    float focal_distance = 20;  // 60 cm

    // Number of samples for depth of field
    int num_samples = 64;

    for (int y = 0; y < _height; y++) {
        for (int x = 0; x < _width; x++) {
            vec3 color(0.0, 0.0, 0.0); // Initialize color accumulator

            for (int s = 0; s < num_samples; s++) {
                // Randomly sample within the aperture
                float rand_x = static_cast<float>(rand()) / RAND_MAX;
                float rand_y = static_cast<float>(rand()) / RAND_MAX;

                // Calculate the offset from the camera position to create the depth of field effect
                vec3 aperture_offset = vec3(rand_x, rand_y, 0.0) * aperture_radius;

                vec3 target = _upper_left + (_lower_left - _upper_left).normalize() * dy * y + (_upper_right - _upper_left).normalize() * dx * x;
                vec3 direction = (target - _position).normalize();
                
                // Calculate the point of focus along the ray
                vec3 focus_point = _position + direction * focal_distance;

                // Offset the camera position to simulate depth of field
                vec3 lens_position = _position + aperture_offset;

                // Create a new ray from the lens_position to the focus point
                Ray ray(lens_position, (focus_point - lens_position).normalize());

                vec3 sample_color = Shade(ray, lights, objects, _background_color, 0, 10);

                color += sample_color;
            }

            // Average the color samples to reduce noise
            color /= static_cast<float>(num_samples);

            Pixel p;
            p.R = color[0] * 255;
            p.G = color[1] * 255;
            p.B = color[2] * 255;

            img.writePixel(x, y, p);
        }
    }

    return img;
}
