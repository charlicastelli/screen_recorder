import pyautogui 
import cv2 
import numpy as np 
from datetime import datetime


# Recebe data e hora atual / converte string
now = datetime.now()
date_time_now = now.strftime("%d%m%Y%H%M%S")


resolution = (1920, 1080) 
codec = cv2.VideoWriter_fourcc(*'mp4v') 
filename = f'Recording{date_time_now}.mp4'
fps = 60.0

  
out = cv2.VideoWriter(filename, codec, fps, resolution) 
cv2.namedWindow("Gravando...", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("Gravando...", 480, 270) 
  
while True: 
    img = pyautogui.screenshot() 
    frame = np.array(img) 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    out.write(frame) 
    cv2.imshow('Gravando...', frame) 

    # Pressionar q para encerrar gravação e sair
    if cv2.waitKey(1) == ord('q'):
        break

out.release() 
cv2.destroyAllWindows()

