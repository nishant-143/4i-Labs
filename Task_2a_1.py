import numpy as np
import cv2
cap = cv2.VideoCapture('/Users/nishanth/Downloads/video_task.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
wait = int(1000/fps)

ret, frame = cap.read()
height, width = frame.shape[:2]
image = np.zeros(frame.shape, np.uint8)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video_3.avi', fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([200, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    out.write(result)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)
    if cv2.waitKey(wait) == ord('q'):
        break

    
cap.release()
out.release()
cv2.destroyAllWindows()
