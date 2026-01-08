#IMPORTANT: Met python versie 3.12 werkt pyautogui niet goed. Gebruik python 3.11 of lager.

import numpy as np
import cv2
import pyautogui

#resolutie
resolution = (1920, 1080)

#fps
fps = 60.0

#codec
codec = cv2.VideoWriter_fourcc(*"XVID")

#output bestand
output_file = "recorded_video.mp4"

#video writer object
out = cv2.VideoWriter(output_file, codec, fps, resolution)


# per iteratie van de loop het scherm vastleggen en opslaan in het output bestand
while True:
    img = pyautogui.screenshot()
    
    # zet de afbeelding om naar een numpy array
    frame = np.array(img)
    
    # zet de kleuren om van BGR naar RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # schrijf het frame naar het output bestand
    out.write(frame)
    
    # opnemen stoppen wanneer 'esc'wordt ingedrukt
    if cv2.waitKey(1) == 27 or cv2.waitKey(1) == ord('q'):
        break
    
    
out.release()
cv2.destroyAllWindows()