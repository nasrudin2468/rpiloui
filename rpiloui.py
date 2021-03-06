################################################################################
#
# rpiloui - a python game engine for hasbros looping loui game controlled via a
#           raspberry pi single board computer
#
# This code is released under: 
#
# Copyright (c) 2020 nasrudin2468
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
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
CODEVERSION    = "0.0.4"
CODEDATE       = "2020-04-17"


################################################################################
# classes / structs

class struct:
    # Class used for struct like data objects without any methods
    def __init__(self, **entries): self.__dict__.update(entries)
               
        
################################################################################
# Import external functions

import src.config   as cfg
import src.game     as game
import src.hwtest   as hwtest
import src.install  as install
import src.motor    as motor

################################################################################
# Functions

def signal_handler(signal, frame):
    sys.exit(0)


################################################################################
# beginn main

# init global vars
cmdupdate = "cd .."

# print welcome msg with app name and build version
print('rpiloui ' + CODEVERSION + ' - ' + CODEDATE)

# check for modules which might not be part of the standard python 3 installation
if 'MissingModule' in locals():
    print('\n One or more Missing Module detected. Install by typing rpiloui -install')
    
# create data object, load config data from configuration file, check for valid data 
# and sanitize if necessary
conf = cfg.objconfig()
#cfg.read(conf)

#cfg.sanitize(conf)


# check for given command line arguments
if len(sys.argv) == 1:
    print('\nNo command line argument given. type rpiloui -help for valid arguments')
    exit()

    
if len(sys.argv) != 1:
    if (sys.argv[1] in ("-help")):
        print("not implemented. ")
        exit()

    elif (sys.argv[1] in ( "-install")):
        install.install()
        exit()
     
    elif (sys.argv[1] in ( "-play")):
        game.start(conf)
        exit()
 
    elif (sys.argv[1] in ( "-update")):
        subprocess.call("chmod u+x ./update.sh", shell=True)    
        subprocess.call("./update.sh", shell=True)
        exit()
  
    elif (sys.argv[1] in ( "-simulate")):
        print("not implemented. ")
        exit()

    elif (sys.argv[1] in ( "-hwtest")):  
        hwtest.hwtest(conf)
        exit()
    
    elif (sys.argv[1] in ( "-demo")):  
        hwtest.demo(conf)
        exit()
    
    else: 
        print('Invalid command line argument given. type rpiloui - help for valid arguments')
        exit()
