import numpy as np
import cv2
cap = cv2.VideoCapture('/Users/nishanth/Downloads/video_task.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
wait = int(1000/fps)

ret, frame = cap.read()
height, width = frame.shape[:2]


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video_2.avi', fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray, sketch = cv2.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    out.write(sketch)
    cv2.imshow('sketch',sketch)
    if cv2.waitKey(wait) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

