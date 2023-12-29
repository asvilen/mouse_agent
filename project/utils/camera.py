import cv2
import os
from uuid import uuid4
from datetime import datetime
import time


class CameraHandler:
    FOLDER_NAME = 'images'

    def __init__(self):
        self.relative_file_path = None
        self.absolute_file_path = None

    async def take_picture(self):
        # Create unique photo id
        photo_id = datetime.now().strftime('%Y%m%d%H%M%S-') + str(uuid4())
        self.relative_file_path = os.path.join(self.FOLDER_NAME, f"{photo_id}.jpg")

        # Image capture logic
        cap = cv2.VideoCapture(0)
        # Allow the camera to stabilize after last shot
        time.sleep(2)
        # Get the photo
        ret, frame = cap.read()
        # Save it
        cv2.imwrite(self.relative_file_path, frame)
        cap.release()

        # full path to file to be saved in db
        self.absolute_file_path = os.path.abspath(self.relative_file_path)
