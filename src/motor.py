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

# function: init(objmotor, arrcfg)
# Initiate motor pwm module using gpiozero and pin configuration from 
# configarray 
#    Input:  objmotor - motorobject containing pwmzero objects, current speed
#            and direction
#            arrcfg - configuration array holding hardware pin adress,
#            pwm frequency, maximum dutycycle and minimum direction deathtime
#    Output: -
def init(objmotor, objcfg):
    # PWM pin Control Objects provided by pgiozero
    objmotor.cw             = gpiozero.output_devices.PWMOutputDevice(objcfg.motor_cw, True, 0, objcfg.pwmfreq, None)
    objmotor.ccw            = gpiozero.output_devices.PWMOutputDevice(objcfg.motor_ccw, True, 0, objcfg.pwmfreq, None)
    objmotor.targetspeed    = 0                 # final motorspeed
    objmotor.acceleration   = 0                 # motor acceleration 
    objmotor.actualspeed    = 0                 # actual motor speed
    objmotor.maxduty        = objcfg.maxduty    # maximum allowed pwm dutycycle
    
    # Activate PWM Outputs
    objmotor.cw.on()
    objmotor.ccw.on()


# function: _set(objmotor, speed)
# set motor speed and direction based on given speed variable
# WARNING: lowlevelfunction: might cause hardware damage since output deathtime
# on direction change and acceleration value are ignored!
#    Input:  objmotor - motorobject containing pwmzero objects, current speed
#            and direction
#            speed - speed of the motor (-1 to 1). positive value: clockwise
#            direction. negative value: counter clockwise direction
#    Output: -
def _set(objmotor, speed):
    
    if (speed > 0):
        # clockwise direction
        objmotor.cw.value  = 1 - abs(speed) * (objmotor.maxduty/100)
        objmotor.ccw.value = 1
    
    elif (speed == 0):
        # motor stop
        objmotor.cw.value  = 1
        objmotor.ccw.value = 1
        
    elif (speed < 0):
        # counterclockwise direction
        objmotor.cw.value  = 1
        objmotor.ccw.value = 1 - abs(speed) * (objmotor.maxduty/100)
        
    objmotor.actualspeed = speed    


