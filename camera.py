#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import subprocess, os
import signal
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
RearView_Switch = 14  # pin 18
GPIO.setup(RearView_Switch,GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "  Press Ctrl & C to Quit"

try:
    
   run = 0
   bright = 0
   while True :
      	time.sleep(0.1)
	#the next four blocks are used for toggeling between the camera views.
      	if GPIO.input(RearView_Switch)==0 and run == 0:
		print "  Started Full screen"
         	rpistr = "python /boot/crankshaft/back-camera.py"
         	p=subprocess.Popen(rpistr,shell=True, preexec_fn=os.setsid)
         	run = 1
         	while GPIO.input(RearView_Switch)==0:
             		time.sleep(0.1)


      	if GPIO.input(RearView_Switch)==0 and run == 1:
         	print "  Stopped " 
         	run = 0
         	os.killpg(p.pid, signal.SIGTERM)
         	while GPIO.input(RearView_Switch)==0:
            		time.sleep(0.1)
	
except KeyboardInterrupt:
  print "  Quit"
  GPIO.cleanup() 
