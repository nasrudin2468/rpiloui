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
    ModulSerialMissing = True

try:
    import gpiozero
except ImportError:
    pass
    ModulgpiozeroMissing = True


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

import lib.config    as cfg


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
if 'ModulSerialMissing' in locals():
    print('\nMissing Module pyserial. Install by typing rpiloui -install')
if 'ModulgpiozeroMissing' in locals():
    print('\nMissing Module gpiozero. Install by typing rpiloui -install')
    
# load config data from configuration file, check for valid data and sanitize
# if necessary
cfg.read(cfg)
cfg.sanitize(cfg)


# check for given command line arguments
if len(sys.argv) == 1:
    print('\nNo command line argument given. type rpiloui -help for valid arguments')
    
    # PWM test
    #motor = gpiozero.output_devices.PWMOutputDevice(2, True, 0, 1, None)
    #motor.value=0.5
    #motor.toggle()

    
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
        print("Installing pyserial via pip... ")
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
        rawtx = input(" - LED test: (enter n if you want to skip this test)")
        if (rawtx != "n"):
            i = 0
            while (i < 140):
                # Todo: implement routine which lights up sequentially all installed APA102 LEDs
                print ("LED:",i)
                time.sleep(0.1)
                i+=1  
            print("   ...done!\n")
            # Todo: Shut off all LEDs
        else:
            print ("test skipped.\n")        
        
        rawtx = ""
        rawtx = input(" - motor test: (enter n if you want to skip this test)")
        if (rawtx != "n"):
            # Todo: Implement routine which uses PWM outputs to check the motor driver hardware
            
            print(" forward speed 50%...")
            time.sleep(1)
            print(" forward speed 100%...")
            time.sleep(1)
            print(" speed 0%...")
            time.sleep(1)
            print(" backward speed 50%...")
            time.sleep(1)
            print(" backward speed 100%...")
            time.sleep(1)
            print(" speed 0%...")
            time.sleep(1)
            print("   ...done!\n")
        else:
            print ("test skipped.\n")
        
        rawtx = ""
        rawtx = input(" - mux input testt: (enter n if you want to skip this test)")
        if (rawtx != "n"):
            print ("   stop mux test by pressing CTRL + C")
            k = 0
            while (1):  
                # TODO: Implement method which periodically scans all muxed inputs, compares
                # the new state to the old ones and reports changes via cmd line, until CTRL + C
                # is pressed
                k = 0
   
        else:
            print ("test skipped.\n")
            
        print("hardware test finished.")
        exit()
    
    else: 
        print('Invalid command line argument given. type rpiloui - help for valid arguments')
        exit()
