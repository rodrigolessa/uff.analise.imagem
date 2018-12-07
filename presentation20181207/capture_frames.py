import sys
import os
import argparse
import cv2

# Test
# python capture_frames.py -f pet_view_008.mp4
# python capture_frames.py -f ..\dataset_pedestrian_crossing\video_0174.mp4

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required = True, help = "Path to the video file")

args = vars(ap.parse_args())

vidcap = cv2.VideoCapture(args["file"])
success, image = vidcap.read()
count = 0

# try to delete the object to avoid compare it self
try:
    #os.remove("videoFrames")
    os.makedirs("videoFrames")
except OSError:
    pass

while success:
    cv2.imwrite("videoFrames\\frame%d.jpg" % count, image) # save frame as JPEG file
    success, image = vidcap.read()
    print(count, ' - Read a new frame: ', success)
    count += 1