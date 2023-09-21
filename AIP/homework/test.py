import cv2
import numpy as np

# Load the original images
# jpeg_image = cv2.imread(r"./中文測試/Lenna.jpg")
jpeg_image = cv2.imdecode(np.fromfile("./中文測試/Lenna.jpg",dtype=np.uint8), cv2.IMREAD_UNCHANGED)
# png_image = cv2.imread(r"./中文測試/pepega.png", cv2.IMREAD_UNCHANGED)  # Preserve alpha channel
png_image = cv2.imdecode(np.fromfile("./中文測試/pepega.png",dtype=np.uint8), cv2.IMREAD_UNCHANGED)
# gray_image = cv2.imread(r"./中文測試/gray_Lenna.png", cv2.IMREAD_GRAYSCALE)
gray_image = cv2.imdecode(np.fromfile("./中文測試/gray_Lenna.png",dtype=np.uint8), cv2.IMREAD_UNCHANGED)

# Encode the images in PPM format
png_image = cv2.cvtColor(png_image, cv2.COLOR_BGRA2BGR)
gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
ret, jpeg_encoded = cv2.imencode(".ppm", jpeg_image)
ret, png_encoded = cv2.imencode(".ppm", png_image)
ret, gray_encoded = cv2.imencode(".ppm", gray_image)

# Save the encoded PPM images to files
if ret:
    with open("output_jpeg.ppm", "wb") as f:
        f.write(jpeg_encoded.tobytes())

    with open("output_png.ppm", "wb") as f:
        f.write(png_encoded.tobytes())

    with open("output_gray.ppm", "wb") as f:
        f.write(gray_encoded.tobytes())
else:
    print("Error encoding images")

print("Images encoded and saved as PPM files.")
