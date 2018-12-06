import numpy as np
import cv2
import os


filename = "OpenCvVideo.avi"
fps=24.0
my_res = '100p'


# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']



#standar video dimensions sizes
STD_DIMENSIONS={
    "480p" : (640, 480),
    "720p" : (1280, 720),
    "1080p" : (1920, 1080),
    "4k" : (3840, 2160),
}
def change_res2(cap,width,height):
    cap.set(3,width)
    cap.set(4,height)

def get_dims(cap, res="1080p"):
    width, height = STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res2(cap,width, height)
    return  width, height


cap = cv2.VideoCapture(0)
dims = get_dims(cap,res=my_res)
video_type_cv2 = get_video_type(filename)
out = cv2.VideoWriter(filename,video_type_cv2,fps,dims)

def make_1080p():
    cap.set(3,1920)
    cap.set(4,1080)

def make_720p():
    cap.set(3,1980)
    cap.set(4,720)

def make_240p():
    cap.set(3,200)
    cap.set(4,100)


def change_res(width,height):
    cap.set(3,width)
    cap.set(4,height)

def rescale_frame(frame,percent=75):
    scale_percent = 75
    width = int(frame.shape[1]*scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation= cv2.INTER_AREA)

while True:
    ret, frame = cap.read()
    out.write(frame)
    frame = rescale_frame(frame,percent=30)



    cv2.imshow('frame1', frame)  # imgshow

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllwindows()