################################################################################
#
# rpiloui - a python game engine for hasbros looping loui game controlled via a
#           raspberry pi single board computer
#
# This code is released under: 
#
# Copyright (c) 2020 nasrudin2468
#
# TODO: licence text
#
################################################################################


################################################################################
# Import Libraries


import array
import binascii
import configparser
import datetime
import io
import logging
import os
import pip
import signal
import subprocess
import sys
import time

try:    
    import serial
except ImportError:
    pass
    MissingModule = True

try:
    import gpiozero
except ImportError:
    pass
    MissingModule = True

try:    
    import apa102_pi
except ImportError:
    pass
    MissingModule = True

################################################################################
# Constants
BUILDVERSION     = "0.0.2"
BUILDDATE         = "2020-03-25"


################################################################################
# classes / structs
    
class sampleclass:
    def __init__(self):
        self.samplevalue=0
               
        
################################################################################
# Import external functions

import lib.config as cfg


################################################################################
# Functions

def signal_handler(signal, frame):
    sys.exit(0)


################################################################################
# beginn main

# init global vars
cmdupdate = "cd .."

# print welcome msg with app name and build version
print('rpiloui ' + BUILDVERSION + ' - ' + BUILDDATE)

# check for modules which might not be part of the standard python 3 installation
if 'MissingModule' in locals():
    print('\n One or more Missing Module detected. Install by typing rpiloui -install')
    
# load config data from configuration file, check for valid data and sanitize
# if necessary
cfg.read(cfg)
cfg.sanitize(cfg)


# check for given command line arguments
if len(sys.argv) == 1:
    print('\nNo command line argument given. type rpiloui -help for valid arguments')
    exit()

    
if len(sys.argv) != 1:
    if (sys.argv[1] in ("-help")):
        print("not implemented. ")
        exit()

    elif (sys.argv[1] in ( "-install")):
        print("Install required libraries. Requires internet connection! Might need admin / root...")

        print("Installing pyserial via pip... ")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyserial"])
        print("Installing gpiozero via pip... ")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gpiozero"])            
        print("Installing apa102-pi via pip... ")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "apa102-pi"])
        exit()
     
    elif (sys.argv[1] in ( "-play")):
        print("not implemented. ")
        exit()
 
    elif (sys.argv[1] in ( "-update")):
        subprocess.call("chmod u+x ./update.sh", shell=True)    
        subprocess.call("./update.sh", shell=True)
        exit()
  
    elif (sys.argv[1] in ( "-simulate")):
        print("not implemented. ")
        exit()

    elif (sys.argv[1] in ( "-hwtest")):  
        print("hardware testmodus.")
        
        rawtx = ""   
        rawtx = input(" - audio test: (enter n if you want to skip this test)")
        if (rawtx != "n"):
            subprocess.call("aplay /usr/share/sounds/alsa/Front_Left.wav", shell=True)
            time.sleep(1)
            subprocess.call("aplay /usr/share/sounds/alsa/Front_Center.wav", shell=True)
            time.sleep(1)
            subprocess.call("aplay /usr/share/sounds/alsa/Front_Right.wav", shell=True)
            
        else:
            print ("test skipped.\n")
        
        rawtx = ""   
        rawtx = input(" - LED test: (enter n if you want to skip this test)")
        if (rawtx != "n"):
            i = 0
            subprocess.call("python3 runcolorcycle.py", shell=True) 
            
            #while (i < 140):
            #    # Todo: implement routine which lights up sequentially all installed APA102 LEDs
            #    print ("LED:",i)
            #    time.sleep(0.1)
            #    i+=1  
            #print("   ...done!\n")
            # Todo: Shut off all LEDs
        else:
            print ("test skipped.\n")        
        
        rawtx = ""
        rawtx = input(" - motor test: (enter n if you want to skip this test)")
        if (rawtx != "n"):
            # Configure gpiozero pwm function
            # gpiozero.PWMOutputDevice(pin, *, active_high=True, initial_value=0, frequency=100, pin_factory=None)
            motor_cw        = gpiozero.output_devices.PWMOutputDevice(cfg.motor_cw, True, 0, cfg.pwmfreq, None)
            motor_ccw       = gpiozero.output_devices.PWMOutputDevice(cfg.motor_ccw, True, 0, cfg.pwmfreq, None)
            
            print(" forward speed 50%...")
            motor_cw.on()
            motor_ccw.on()
            motor_cw.value  = 0.5*(cfg.maxduty/100)
            motor_ccw.value = 1
            time.sleep(2)
            print(" forward speed 100%...")
            motor_cw.value  = 0*(cfg.maxduty/100)
            time.sleep(2)
            print(" speed 0%...")
            #motor_cw.off()
            #motor_ccw.off()
            motor_cw.value = 1
            motor_ccw.value = 1
            time.sleep(1)
            print(" backward speed 50%...")
            motor_cw.value  = 1
            motor_ccw.value = 0.5*(cfg.maxduty/100)
            #motor_cw.off()
            #motor_ccw.on()
            time.sleep(2)
            print(" backward speed 100%...")
            motor_ccw.value = 0
            time.sleep(2)
            print(" speed 0%...")
            #motor_cw.off()
            #motor_ccw.off()
            motor_cw.value  = 1
            motor_ccw.value  = 1
            time.sleep(1)
            print("   ...done!\n")
        else:
            print ("test skipped.\n")
        
        rawtx = ""
        rawtx = input(" - mux input test: (enter n if you want to skip this test)")
        if (rawtx != "n"):
            print ("   stop mux test by pressing CTRL + C")
            mux_a = gpiozero.DigitalOutputDevice(cfg.mux_coin, True, False, None)
            mux_b = gpiozero.DigitalOutputDevice(cfg.mux_tilt, True, False, None)
            mux_c = gpiozero.DigitalOutputDevice(cfg.mux_action, True, False, None)
            
            in0 = gpiozero.InputDevice(cfg.mux_0, True, None, None)
            in1 = gpiozero.InputDevice(cfg.mux_1, True, None, None)
            in2 = gpiozero.InputDevice(cfg.mux_2, True, None, None)
            in3 = gpiozero.InputDevice(cfg.mux_3, True, None, None)
            in4 = gpiozero.InputDevice(cfg.mux_4, True, None, None)
            in5 = gpiozero.InputDevice(cfg.mux_5, True, None, None)
            in6 = gpiozero.InputDevice(cfg.mux_6, True, None, None)
            in7 = gpiozero.InputDevice(cfg.mux_7, True, None, None)
            while (1): 
                # TODO: Implement method which periodically scans all muxed inputs, compares
                # the new state to the old ones and reports changes via cmd line, until CTRL + C
                # is pressed
                k = 0
                
                
                mux_a.on()
                print("mux A")
                time.sleep(0.1)
                listmux_a = [in0.is_active,in1.is_active, in2.is_active, in3.is_active, in4.is_active, in5.is_active, in6.is_active, in7.is_active]
                print(listmux_a)
                time.sleep(1)
                mux_a.off()
                mux_b.on()
                #print("mux B")
                time.sleep(0.1)
                listmux_a = [in0.is_active,in1.is_active, in2.is_active, in3.is_active, in4.is_active, in5.is_active, in6.is_active, in7.is_active]
                print(listmux_a)
                
                time.sleep(1)
                mux_b.off()
                mux_c.on()
                #print("mux C")
                time.sleep(0.1)
                listmux_a = [in0.is_active,in1.is_active, in2.is_active, in3.is_active, in4.is_active, in5.is_active, in6.is_active, in7.is_active]
                print(listmux_a)
                time.sleep(1)
                mux_c.off()
                mux_c.off()
                
        else:
            print ("test skipped.\n")
            
        print("hardware test finished.")
        
        exit()
    
    else: 
        print('Invalid command line argument given. type rpiloui - help for valid arguments')
        exit()
