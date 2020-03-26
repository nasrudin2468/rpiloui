################################################################################
#
# rpiloui - a python game engine for hasbros looping loui game controlled via a
#           raspberry pi single board computer
#
# This code is released under: 
#
# Copyright (c) 2019 nasrudin2468
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
import signal
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
import subprocess

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
    
# load config data from configuration file
cfg.read(cfg)


# check for given command line arguments
if len(sys.argv) == 1:
    print('\nNo command line argument given. type rpiloui -help for valid arguments')
    
    # PWM test
    #motor = gpiozero.output_devices.PWMOutputDevice(2, True, 0, 1, None)
    #motor.value=0.5
    #motor.toggle()
    
    
    rawtx = input("press enter to exit")
    exit()
    
if len(sys.argv) != 1:
    if (sys.argv[1] in ("-help")):
        print("\nnot implemented. ")
        #arg.help()
        exit()
        
    elif (sys.argv[1] in ( "-install")):
        #arg.install()
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
    
    elif (sys.argv[1] in ( "-run-unittests")):    
        print("not implemented. ")
        exit()
        
    elif (sys.argv[1] in ( "-hwtest")):    
        print("not implemented. ")
        exit()
    
        
    else: 
        print('Invalid command line argument given. type rpiloui - help for valid arguments')
        exit()

