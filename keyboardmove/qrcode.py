import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from PIL import Image
import ipywidgets.widgets as widgets

#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

#Set GPIO port to BCM coding mode
GPIO.setmode(GPIO.BCM)

#Ignore the warning message
GPIO.setwarnings(False)

#Define motor pin
IN1 = 19
IN2 = 26
IN3 = 20
IN4 = 21
ENA = 13
ENB = 16

image_widget = widgets.Image(format='jpeg', width=320, height=240)
display(image_widget)
