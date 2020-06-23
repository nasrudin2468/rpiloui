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

import datetime
import gpiozero

################################################################################
# Constants


################################################################################
# classes / structs

class state:
    def __init__(self):
        # Define arrays for current processed status
        self.coin      = [0, 0, 0, 0, 0, 0, 0, 0]
        self.tilt      = [0, 0, 0, 0, 0, 0, 0, 0]
        self.action    = [0, 0, 0, 0, 0, 0, 0, 0]
        self.time      = 0 # timestamp for last change of current state

class mapinput:
    def __init__(self, objcfg):
        # Define arrays for logical mapping from mux inputs to  connected actors
        self.coinsensor    = objcfg.mapinput.coinsensor
        self.tiltsensor    = objcfg.mapinput.tiltsensor
        self.actionbutton  = objcfg.mapinput.actionbutton

class muxiofunc:
    def __init__(self, objcfg):
        # Initiate mux control output pins using gpiozero
        self.coin           = gpiozero.DigitalOutputDevice(objcfg.mux_coin, True, False, None)
        self.tilt           = gpiozero.DigitalOutputDevice(objcfg.mux_tilt, True, False, None)
        self.action         = gpiozero.DigitalOutputDevice(objcfg.mux_action, True, False, None)
        
        # Initiate mux input pins using gpiozero
        self.input      = [None] * 8
        self.input[0]   = gpiozero.InputDevice(objcfg.mux.input[0], True, None, None)
        self.input[1]   = gpiozero.InputDevice(objcfg.mux.input[1], True, None, None)
        self.input[2]   = gpiozero.InputDevice(objcfg.mux.input[2], True, None, None)
        self.input[3]   = gpiozero.InputDevice(objcfg.mux.input[3], True, None, None)
        self.input[4]   = gpiozero.InputDevice(objcfg.mux.input[4], True, None, None)
        self.input[5]   = gpiozero.InputDevice(objcfg.mux.input[5], True, None, None)
        self.input[6]   = gpiozero.InputDevice(objcfg.mux.input[6], True, None, None)
        self.input[7]   = gpiozero.InputDevice(objcfg.mux.input[7], True, None, None)
        
class muxiodata:
    def __init__(self, objcfg):
        # Define arrays for current and last processed status
        self.currentstate   = state()
        self.laststate      = state()
            
        # Define arrays for logical mapping from mux inputs to  connected actors   
        self.mapinput       = mapinput(objcfg)
        
        
       
        
        
################################################################################
# Import external functions


# Prevent direct access to this file since it would be useless
if __name__ == '__main__':
    exit()


################################################################################
# Functions
    

# function: poll(objmuxio):
# Scan all inputs in every mux configuration and write timestamp and its status 
# into current state array using logical mapping  
#    Input:  objmuxio - muxio object containing gpio objects and current input
#            and last processed input status
#
#    Output: -
def poll(objmuxio, funcmuxio):
    # Update timestamp
    objmuxio.currentstate.time      = datetime.datetime.now()
    
    # Prepare MUX control to read out coin sensors
    funcmuxio.coin.on()
    funcmuxio.tilt.off()
    funcmuxio.action.off()
    
    # Read Inputs muxed to coin sensors and save values in correct place using mapinput
    for i in range(0, 8, 1):
        objmuxio.currentstate.coin[i] = int(funcmuxio.input[objmuxio.mapinput.coinsensor [i]].is_active) 
        
    # Prepare MUX control to read out tilt sensors
    funcmuxio.coin.off()
    funcmuxio.tilt.on()
    funcmuxio.action.off()
    
    # Read Inputs muxed to tilt sensors and save values in correct place using mapinput
    for i in range(0, 8, 1):
        objmuxio.currentstate.tilt[i] = int(funcmuxio.input[objmuxio.mapinput.tiltsensor [i]].is_active)
        
    # Prepare MUX control to read out action buttons
    funcmuxio.coin.off()
    funcmuxio.tilt.off()
    funcmuxio.action.on()
    
    # Read Inputs muxed to action button and save values in correct place using mapinput
    for i in range(0, 8, 1):
        objmuxio.currentstate.action[i] = int(funcmuxio.input[objmuxio.mapinput.actionbutton [i]].is_active)
    
    # Deactivate MUX in order to reduce electric load on PSU
    funcmuxio.coin.off()
    funcmuxio.tilt.off()    
    funcmuxio.action.off()
    

# function: update(objmuxio):
# updates last current state after reading inputs 
#    Input:  objmuxio - muxio object containing gpio objects and current input
#            and last processed input status
#    Output: -
def update(objmuxio):
    # Update timestamp
    objmuxio.laststate.time      = datetime.datetime.now()
    
    # Copy Current values into laststate
    objmuxio.laststate.coin     = objmuxio.currentstate.coin[:]
    objmuxio.laststate.tilt     = objmuxio.currentstate.tilt[:]
    objmuxio.laststate.action   = objmuxio.currentstate.action[:]

    
# function: debugreaddelta(objmuxio):
# Analyse MUX object and print status of changed inputs via cmd line
#    Input:  objmuxio - muxio object containing gpio objects and current input
#            and last processed input status
#    Output: -
def debugreaddelta(objmuxio):

    # Check coin sensors
    for i in range(0, 8, 1):
        if objmuxio.currentstate.coin[i] > objmuxio.laststate.coin[i]:
            print("- Coin sensor ", i, ": Coin vanished!")
        
        elif objmuxio.currentstate.coin[i] < objmuxio.laststate.coin[i]:
            print("- Coin sensor ", i, ": Coin detected.")
        
    # Check tilt sensors
    for i in range(0, 8, 1):
        if objmuxio.currentstate.tilt[i] > objmuxio.laststate.tilt[i]:
            print("- Tilt Sensor ", i, ": lever released.")
        
        elif objmuxio.currentstate.tilt[i] < objmuxio.laststate.tilt[i]:
            print("- Tilt Sensor ", i, ": lever pressed!")
    

    # Check action buttons
    for i in range(0, 8, 1):
        if objmuxio.currentstate.action[i] > objmuxio.laststate.action[i]:
            print("- Action button ", i, ": pressed!")
        
        elif objmuxio.currentstate.action[i] < objmuxio.laststate.action[i]:
            print("- Action button ", i, ": released")
        
        
