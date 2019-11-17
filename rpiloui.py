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


################################################################################
# Constants
BUILDVERSION     = "0.0.1"
BUILDDATE         = "2019-11-17"


################################################################################
# classes / structs
    
class sampleclass:
    def __init__(self):
        self.samplevalue=0
               
        
################################################################################
# Import external functions

# import lib.message    as msg
# import lib.config    as cfg

################################################################################
# Functions

def signal_handler(signal, frame):
    sys.exit(0)


################################################################################
# beginn main

# init global vars

# load config data from configuration file
# cfg.read(cfg)

if len(sys.argv) == 1:
    print('\nrpiloui ' + BUILDVERSION + ' - ' + BUILDDATE)
    
    # check for modules which might not be part of the standard python 3 installation
    if 'ModulSerialMissing' in locals():
        print('Missing Module pyserial. Install by typing pye-motion -install')
        
    print('No command line argument given. type pye-motion -help for valid arguments')
    
if len(sys.argv) != 1:
    if (sys.argv[1] in ("-help")):
        print("not implemented. ")
        #arg.help()
        exit()
        
    elif (sys.argv[1] in ( "-install")):
        #arg.install()
        exit()
        
    elif (sys.argv[1] in ( "-play")):
        print("not implemented. ")
        exit()
    
    elif (sys.argv[1] in ( "-simulate")):
        print("not implemented. ")
        exit()
    
    elif (sys.argv[1] in ( "-run-unittests")):    
        print("not implemented. ")
        exit()
    
        
    else: 
        print('Invalid command line argument given. type pye-motion - help for valid arguments')

