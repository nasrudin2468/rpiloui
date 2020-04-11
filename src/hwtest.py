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
import subprocess
import time


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

# function:  hwtest(arrcfg)
# reads config file and saves variables into given array
#    Input:  name of array containing hardware configuration
#    Output: -
def hwtest(arrcfg):    
    print("hardware testmodus.")
        
    rawtx = ""   
    rawtx = input(" - audio test: (enter n if you want to skip this test)")
    if (rawtx != "n"):
        subprocess.call("aplay ./user/audiofiles/audiotest.wav", shell=True)
            
    else:
        print ("test skipped.\n")
    
    rawtx = ""   
    rawtx = input(" - LED test: (enter n if you want to skip this test)")
    if (rawtx != "n"):
        i = 0
        subprocess.call("python3 ./lib/_runcolorcycle.py", shell=True )
            
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
        motor_cw        = gpiozero.output_devices.PWMOutputDevice(arrcfg.motor_cw, True, 0, arrcfg.pwmfreq, None)
        motor_ccw       = gpiozero.output_devices.PWMOutputDevice(arrcfg.motor_ccw, True, 0, arrcfg.pwmfreq, None)
            
        print(" forward speed 50%...")
        motor_cw.on()
        motor_ccw.on()
        motor_cw.value  = 0.5*(arrcfg.maxduty/100)
        motor_ccw.value = 1
        time.sleep(2)
        print(" forward speed 100%...")
        motor_cw.value  = 0*(arrcfg.maxduty/100)
        time.sleep(2)
        print(" speed 0%...")
        #motor_cw.off()
        #motor_ccw.off()
        motor_cw.value = 1
        motor_ccw.value = 1
        time.sleep(1)
        print(" backward speed 50%...")
        motor_cw.value  = 1
        motor_ccw.value = 0.5*(arrcfg.maxduty/100)
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
        mux_a = gpiozero.DigitalOutputDevice(arrcfg.mux_coin, True, False, None)
        mux_b = gpiozero.DigitalOutputDevice(arrcfg.mux_tilt, True, False, None)
        mux_c = gpiozero.DigitalOutputDevice(arrcfg.mux_action, True, False, None)
            
        in0 = gpiozero.InputDevice(arrcfg.mux_0, True, None, None)
        in1 = gpiozero.InputDevice(arrcfg.mux_1, True, None, None)
        in2 = gpiozero.InputDevice(arrcfg.mux_2, True, None, None)
        in3 = gpiozero.InputDevice(arrcfg.mux_3, True, None, None)
        in4 = gpiozero.InputDevice(arrcfg.mux_4, True, None, None)
        in5 = gpiozero.InputDevice(arrcfg.mux_5, True, None, None)
        in6 = gpiozero.InputDevice(arrcfg.mux_6, True, None, None)
        in7 = gpiozero.InputDevice(arrcfg.mux_7, True, None, None)
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
    