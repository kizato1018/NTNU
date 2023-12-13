import cv2
import time

cap = cv2.VideoCapture(0)  # Change 0 to the desired camera index or video file path
frame_cnt = 0
start_time = time.time()
fps = 0
while True:

    _, frame = cap.read()
    frame_cnt += 1
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Your image processing code goes here

    # Calculate FPS
    if time.time() - start_time >= 0.1:
        fps = frame_cnt / (time.time() - start_time)
        start_time = time.time()
        frame_cnt = 0

    # Display FPS at the right corner
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
