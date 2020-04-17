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
               
        
################################################################################
# Import external functions


# Prevent direct access to this file since it would be useless
if __name__ == '__main__':
    exit()

################################################################################
# Functions

# function: init(objmuxio, objcfg)
# Initiate mux input using gpiozero and pin configuration from configarray 
#    Input:  objmuxio - muxio object containing gpio objects and current input
#            and last processed input status
#            objcfg - data object holding hardware pin adresses and
#            sensor mux mapping
#    Output: -
def init(objmuxio, objcfg):
    # Initiate mux control output pins using gpiozero
    objmuxio.coin       = gpiozero.DigitalOutputDevice(objcfg.mux_coin, True, False, None)
    objmuxio.tilt       = gpiozero.DigitalOutputDevice(objcfg.mux_tilt, True, False, None)
    objmuxio.action     = gpiozero.DigitalOutputDevice(objcfg.mux_action, True, False, None)
    
    # Initiate mux input pins using gpiozero
    objmuxio.input      = [None] * 8
    objmuxio.input[0]   = gpiozero.InputDevice(objcfg.mux.input[0], True, None, None)
    objmuxio.input[1]   = gpiozero.InputDevice(objcfg.mux.input[1], True, None, None)
    objmuxio.input[2]   = gpiozero.InputDevice(objcfg.mux.input[2], True, None, None)
    objmuxio.input[3]   = gpiozero.InputDevice(objcfg.mux.input[3], True, None, None)
    objmuxio.input[4]   = gpiozero.InputDevice(objcfg.mux.input[4], True, None, None)
    objmuxio.input[5]   = gpiozero.InputDevice(objcfg.mux.input[5], True, None, None)
    objmuxio.input[6]   = gpiozero.InputDevice(objcfg.mux.input[6], True, None, None)
    objmuxio.input[7]   = gpiozero.InputDevice(objcfg.mux.input[7], True, None, None)
    
    # Define arrays for current and last processed status
    objmuxio.currentstate           = type('', (), {})
    objmuxio.currentstate.coin      = [0, 0, 0, 0, 0, 0, 0, 0]
    objmuxio.currentstate.tilt      = [0, 0, 0, 0, 0, 0, 0, 0]
    objmuxio.currentstate.action    = [0, 0, 0, 0, 0, 0, 0, 0]
    objmuxio.laststate           = type('', (), {})
    objmuxio.laststate.coin         = [0, 0, 0, 0, 0, 0, 0, 0]
    objmuxio.laststate.tilt         = [0, 0, 0, 0, 0, 0, 0, 0]
    objmuxio.laststate.action       = [0, 0, 0, 0, 0, 0, 0, 0]
    
    objmuxio.currentstate.time      = 0 # timestamp for last change of current state
    objmuxio.laststate.time         = 0 # timestamp for last change of last state
    
    # Define arrays for logical mapping from mux inputs to  connected actors
    objmuxio.mapinput               = type('', (), {})
    objmuxio.mapinput.coinsensor    = objcfg.mapinput.coinsensor
    objmuxio.mapinput.tiltsensor    = objcfg.mapinput.tiltsensor
    objmuxio.mapinput.actionbutton  = objcfg.mapinput.actionbutton
    

# function: poll(objmuxio):
# Scan all inputs in every mux configuration and write timestamp and its status 
# into current state array using logical mapping  
#    Input:  objmuxio - muxio object containing gpio objects and current input
#            and last processed input status
#
#    Output: -
def poll(objmuxio):
    # Update timestamp
    objmuxio.currentstate.time      = datetime.datetime.now()
    
    # Prepare MUX control to read out coin sensors
    objmuxio.coin.on()
    objmuxio.tilt.off()
    objmuxio.action.off()
    
    # Read Inputs muxed to coin sensors and save values in correct place using mapinput
    for i in range(0, 8, 1):
        objmuxio.currentstate.coin[i] = int(objmuxio.input[objmuxio.mapinput.coinsensor [i]].is_active) 
        
    # Prepare MUX control to read out tilt sensors
    objmuxio.coin.off()
    objmuxio.tilt.on()
    objmuxio.action.off()
    
    # Read Inputs muxed to tilt sensors and save values in correct place using mapinput
    for i in range(0, 8, 1):
        objmuxio.currentstate.tilt[i] = int(objmuxio.input[objmuxio.mapinput.tiltsensor [i]].is_active)
        
    # Prepare MUX control to read out action buttons
    objmuxio.coin.off()
    objmuxio.tilt.off()
    objmuxio.action.on()
    
    # Read Inputs muxed to action button and save values in correct place using mapinput
    for i in range(0, 8, 1):
        objmuxio.currentstate.action[i] = int(objmuxio.input[objmuxio.mapinput.actionbutton [i]].is_active)
    
    # Deactivate MUX in order to reduce electric load on PSU
    objmuxio.coin.off()
    objmuxio.tilt.off()    
    objmuxio.action.off()
    

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
        
        
