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

import subprocess
import time


################################################################################
# Constants


################################################################################
# classes / structs


################################################################################
# Import external functions

import motor
import muxio


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
    
    rawtx = input(" - motor test: (enter n if you want to skip this test)")
    if (rawtx != "n"):
        motor.init(motor, arrcfg)
        i = 0
        k = 0
        
        # Speed motor up from 0% to 100% clockwise
        while (i < 100):
            print ("Motor Speed [%]: ",i)
            if (i == 0):
                k = 0
            else:
                k = (i/100)
                
            motor._set(motor, (k))
            time.sleep(0.05)
            i+=1  
        
        
        # Decrease motor speed from +100% clockwise to -100% (counterclockwise)
        while (i > -100):
            print ("Motor Speed [%]: ",i)
            if (i == 0):
                k = 0
            else:
                k = (i/100)
                
            motor._set(motor, (k))
            time.sleep(0.05)
            i-= 1 
        
        
        # Decrease motor speed from -100% (counterclockwise) to 0%
        while (i < 0):
            print ("Motor Speed [%]: ",i)
            if (i == 0):
                k = 0
            else:
                k = (i/100)
                
            motor._set(motor, (k))
            time.sleep(0.05)
            i+= 1
        
        motor._set(motor, (0))
        print("   ...done!\n")
    else:
        print ("test skipped.\n")
        

    rawtx = input(" - mux input test: (enter n if you want to skip this test)")
    if (rawtx != "n"):
        muxio.init(muxio, arrcfg)
        testtime = time.time()+60
        
        while (time.time() < testtime):
            muxio.poll(muxio)
            muxio.debugreaddelta(muxio)
            muxio.update(muxio)
                
    else:
        print ("test skipped.\n")
            
    print("hardware test finished.")
    