import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
font = 'NotoSansTC-Regular.ttf'
last_time_check = 0
check_cooldown = 0.01
frame_cnt = 0
start_time = time.time()
fps = 0
def draw_chinese_text_on_image(opencv_image, text, position, font_path, font_size, color):
    # 將 OpenCV 影像轉換為 PIL 影像
    cv2_im_rgb = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)

    # 使用 PIL 來繪製文字
    draw = ImageDraw.Draw(pil_im)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, font=font, fill=color)

    # 將 PIL 影像轉回 OpenCV 影像
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    
    return cv2_im_processed

def calculate_angle(a, b, c):
    a = np.array([a.x, a.y, a.z])  # First
    b = np.array([b.x, b.y, b.z])  # Mid
    c = np.array([c.x, c.y, c.z])  # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180.0:
        angle = 360-angle
        
    return angle

def get_face_direction(face_landmarks):
    # Get key landmarks
    # print(face_landmarks)
    try:
        nose_tip = face_landmarks.landmark[mp_holistic.PoseLandmark.NOSE]
        left_eye = face_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EYE]
        right_eye = face_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_EYE]
    except:
        print("can't get face")

    # Convert landmarks to numpy arrays
    nose_tip = np.array([nose_tip.x, nose_tip.y, nose_tip.z])
    left_eye = np.array([left_eye.x, left_eye.y, left_eye.z])
    right_eye = np.array([right_eye.x, right_eye.y, right_eye.z])

    # print(f"left_eye_inner {left_eye}")
    # print(f"right_eye_inner {right_eye}")
    # Calculate the vector from right eye to left eye
    eye_vector = left_eye - right_eye
    # eye_vector[1] = 0
    eye_vector_normalized = eye_vector / np.linalg.norm(eye_vector)
    # print(f"eye_vector_normalized {eye_vector_normalized}")

    # Define the y-axis vector (assuming y-axis is up in the coordinate system)
    y_axis = np.array([0, 1, 0])

    # Calculate the cross product to get the face direction vector
    face_direction_vector = np.cross(eye_vector, y_axis)

    # Normalize the face direction vector
    face_direction_normalized = face_direction_vector / np.linalg.norm(face_direction_vector)
    # print(f"face_direction_normalized {face_direction_normalized}")

    # Define the negative z-axis vector (facing towards the screen)
    z_axis = np.array([1, 0, 0])

    # Calculate the angle using the dot product
    dot_product = np.dot(face_direction_normalized, z_axis)
    angle = np.arccos(dot_product)

    # Convert the angle from radians to degrees
    angle_degrees = np.degrees(angle) - 90
    # print(f"angle_degrees {angle_degrees}")
    if angle_degrees < -30:
       face_direction = "Turn Left"
    elif angle_degrees > 30:
       face_direction = "Turn Right"
    else:
       face_direction = "Forward"

    return angle_degrees

def classify(landmarks):
    # try:
    face_direction = get_face_direction(landmarks.pose_landmarks)
    nose = landmarks.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE]
    left_wrist = landmarks.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_WRIST]
    right_wrist = landmarks.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST]
    left_elbow = landmarks.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_ELBOW]
    right_elbow = landmarks.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ELBOW]
    left_shoulder = landmarks.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER]
    right_shoulder = landmarks.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER]
    left_hip = landmarks.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_HIP]
    right_hip = landmarks.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HIP]
    left_arm_angle = calculate_angle(left_wrist, left_elbow, left_shoulder)
    right_arm_angle = calculate_angle(right_wrist, right_elbow, right_shoulder)
    chest_y = (left_hip.y + left_shoulder.y + right_hip.y + right_shoulder.y) * 0.25
    neck_y = (nose.y + (left_shoulder.y + right_shoulder.y) / 2) / 2
    # except:
    #     return 
   #  print(f'nose: {nose.x, nose.y, nose.z}')
   #  print(f'left_wrist: {left_wrist.x, left_wrist.y, left_wrist.z}')
   #  print(f'right_wrist: {right_wrist.x ,right_wrist.y, right_wrist.z}')
   #  print(f'left_elbow: {left_elbow.x, left_elbow.y, left_elbow.z}')
   #  print(f'right_elbow: {right_elbow.x, right_elbow.y, right_elbow.z}')
   #  print(f'left_shoulder: {left_shoulder.x, left_shoulder.y, left_shoulder.z}')
   #  print(f'right_shoulder: {right_shoulder.x, right_shoulder.y, right_shoulder.z}')
   #  print(f'left_hip: {left_hip.x, left_hip.y, left_hip.z}')
   #  print(f'right_hip: {right_hip.x, right_hip.y, right_hip.z}')
   #  print(f'left_arm_angle: {left_arm_angle}')
   #  print(f'right_arm_angle: {right_arm_angle}')
   #  print(f'chest_y: {chest_y}')
   #  print(f'face_direction: {face_direction}')
    
    
    if left_wrist.y > chest_y and right_wrist.y < neck_y and right_arm_angle < 150 and face_direction < -20:
       return "右方來車停止"
       return "Pose 3"
    
    if left_wrist.y < neck_y and right_wrist.y > chest_y and left_arm_angle < 150 and face_direction > 20:
       return "左方來車停止"
       return "Pose 4"
    
    if left_wrist.y < neck_y and right_wrist.y < chest_y and right_arm_angle < 100 and left_arm_angle < 100 and face_direction < 20:
       return "右方來車左轉彎"
       return "Pose 8"
    
    
    if left_wrist.y > chest_y and right_wrist.y < neck_y and right_arm_angle < 150:
       return "前方來車停止"
       return "Pose 2"
    
    if left_wrist.y < chest_y and right_wrist.y < chest_y and left_arm_angle > 150 and right_arm_angle > 150:
       return "前後車輛停止，左右車輛通行"
       return "Pose 1"
    
    
    if left_wrist.y < chest_y and right_wrist.y < chest_y and left_arm_angle > 150 and right_arm_angle < 100:
       return "右方來車通行"
       return "Pose 6"
    
    if left_wrist.y < chest_y and right_wrist.y < neck_y and right_arm_angle < 120 and left_arm_angle < 100:
       return "左方來車左轉彎"
       return "Pose 7"

    if left_wrist.y < chest_y and right_wrist.y < chest_y and left_arm_angle < 70 and right_arm_angle > 150:
       return "左方來車通行"
       return "Pose 5"
    
    if right_wrist.y < nose.y and right_arm_angle > 150:
       return "全部車輛停止"
       return "Pose 0"
    
    
    return "No Pose"

# For static images:
IMAGE_FILES = ['pose0.png', 'pose1.png', 'pose2.png', 'pose3.png', 'pose4.png', 'pose5.png', 'pose6.png', 'pose7.png', 'pose8.png']
BG_COLOR = (192, 192, 192) # gray
cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as holistic:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
    frame_cnt += 1
    # Convert the BGR image to RGB before processing.
    h, w, c = image.shape
    w = w // 5
    h = h // 5
    image = cv2.resize(image, (w, h))
    image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    # 均衡化 Y 通道
   #  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
   #  image_yuv[:, :, 0] = clahe.apply(image_yuv[:, :, 0])

    image.flags.writeable = False
    image = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)
    results = holistic.process(image)
   #  results.pose_landmarks = 
   
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    annotated_image = image.copy()

   
    if results.pose_landmarks and time.time() - last_time_check > check_cooldown:
        # if idx == 3:
        #     print("face:",results.face_landmarks)
        #     print("pose:",results.pose_landmarks)
        #   print("Face Direction:", get_face_direction(results.pose_landmarks))
        text = classify(results)
      #   print("Pose: ", text)
        last_time_check = time.time()

    
    #   print(
    #       f'Pose landmarks: (',
    #       results.pose_landmarks

    #   )

        
        # Draw segmentation on the image.
        # To improve segmentation around boundaries, consider applying a joint
        # bilateral filter to "results.segmentation_mask" with "image".
        # condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        # bg_image = np.zeros(image.shape, dtype=np.uint8)
        # bg_image[:] = BG_COLOR
        # annotated_image = np.where(condition, annotated_image, bg_image)
        # Draw pose, left and right hands, and face landmarks on the image.
      #   mp_drawing.draw_landmarks(
      #       annotated_image,
      #       results.face_landmarks,
      #       mp_holistic.FACEMESH_TESSELATION,
      #       landmark_drawing_spec=None,
      #       connection_drawing_spec=mp_drawing_styles
      #       .get_default_face_mesh_tesselation_style())
        mp_drawing.draw_landmarks(
            annotated_image,
            results.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.
            get_default_pose_landmarks_style())
        
        # cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
    
      #   font = cv2.FONT_HERSHEY_SIMPLEX
        

        # Add text to the image
      #   cv2.putText(annotated_image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
         

    # Plot pose world landmarks.
    # mp_drawing.plot_landmarks(
    #     results.pose_world_landmarks, mp_holistic.POSE_CONNECTIONS)
   
    font_scale = 70  # You might need to adjust this for a size of 50
    color = (0, 0, 0)  # White color
    thickness = 5  # Thickness of the text
    position = (20, 20)  # Position of text (x, y)
    annotated_image = draw_chinese_text_on_image(annotated_image, text, position, font, font_scale, color)
    if time.time() - start_time >= 0.1:
        fps = frame_cnt / (time.time() - start_time)
        start_time = time.time()
        frame_cnt = 0
    print(fps)
    cv2.putText(annotated_image, f"FPS: {fps:.2f}", (w - 200, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    start_time = time.time()
    cv2.imshow('MediaPipe Holistic', annotated_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      cap.release()
      cv2.destroyAllWindows()
      break