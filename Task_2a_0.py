import numpy as np
import cv2
cap = cv2.VideoCapture('/Users/nishanth/Downloads/video_task.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
wait = int(1000/fps)

ret, frame = cap.read()
height, width = frame.shape[:2]
image = np.zeros(frame.shape, np.uint8)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video_1.avi', fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = smaller_frame
    image[height//2:, :width//2] = cv2.flip(smaller_frame,0)
    image[:height//2, width//2:] = cv2.flip(smaller_frame,1)  
    image[height//2:, width//2:] = cv2.flip(smaller_frame,-1)
    out.write(image)
    cv2.imshow('frame', image)
    if cv2.waitKey(wait) == ord('q'):
        break

    
cap.release()
out.release()
cv2.destroyAllWindows()