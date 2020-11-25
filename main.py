#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
#import argparse
import full
import cv2

#print(cv2.__version__)
def extractImages(vidPath, imgPath):
  print("Extraction des frames de la séquence vidéos...")
  count = 0
  vidcap = cv2.VideoCapture(vidPath)
  success,image = vidcap.read()
  while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*500))     
    success,image = vidcap.read()
    #print ('Nouveau frame: ', success)
    cv2.imwrite( imgPath + "frame%d.jpg" % count, image)    
    count = count + 1
  print("Nombre des Frames extraits : 9")

extractImages("test_videos/video_test.mp4", "test_images/") 

full.execute_LAPI('test_images/test2.jpg')

""" for num in range(3):
  try:
    full.execute_LAPI('test_images/frame{0}.jpg'.format(num));
  except:
    print(".....")
 """

