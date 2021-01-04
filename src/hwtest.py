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
import multiprocessing as mp
from apa102_pi.driver import apa102

################################################################################
# Constants


################################################################################
# classes / structs


################################################################################
# Import external functions

from . import motor
from . import muxio


# Prevent direct access to this file since it would be useless
if __name__ == '__main__':
    exit()


################################################################################
# Functions

# function:  hwtest(arrcfg)
# reads config file and saves variables into given array
#    Input:  name of array containing hardware configuration
#    Output: -
def hwtest(objcfg):    
    print("hardware testmodus.")
    
    # Initiate hardware first
    motor.init(motor, objcfg)
    #muxio.init(muxio, objcfg)
    objmuxio = muxio.muxiodata(objcfg)      # create mux data object
    funcmuxio = muxio.muxiofunc(objcfg)     # create mux control object
    objledfunc = apa102.APA102(num_led=152, global_brightness=20, mosi=10, sclk=11, order='rgb')
        
    rawtx = input(" - audio test: (enter n if you want to skip this test)")
    if (rawtx != "n"):
        subprocess.call("aplay ./user/audiofiles/audiotest.wav", shell=True)
            
    else:
        print ("test skipped.\n")
    
    rawtx = ""   
    rawtx = input(" - LED test: (enter n if you want to skip this test)")
    if (rawtx != "n"):
        k = 0
        while (k < 9):
            i = 0
            while (i < 152):
                objledfunc.set_pixel(i, 255, 255, 255, 50)
                i+=1
            objledfunc.show()
            time.sleep(0.01)
            objledfunc.clear_strip()
            time.sleep(0.01)
            k+=1
        
        
        i = 0
        while (i < 152):
            objledfunc.set_pixel(i, 0, 0, 255, 50)
            objledfunc.show()
            i+=1 
        time.sleep(2)
        i = 0
        while (i < 152):
            objledfunc.set_pixel(i, 0, 255, 0, 50)
            objledfunc.show()
            i+=1 
        time.sleep(2)
        i = 0
        while (i < 152):
            objledfunc.set_pixel(i, 255, 0, 0, 50)
            objledfunc.show()
            i+=1 
        time.sleep(2)
        objledfunc.clear_strip()
            
            
    else:
        print ("test skipped.\n")        
    
    rawtx = input(" - motor test: (enter n if you want to skip this test)")
    if (rawtx != "n"):
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
        testtime = time.time()+30               # Run test for 30 seconds
        muxio.update(objmuxio)                  # Update to inital state since different actors have different Idle states
        
        while (time.time() < testtime):
            muxio.poll(objmuxio, funcmuxio)     # poll actual muxdata
            muxio.debugreaddelta(objmuxio)      # report changed values via console
            muxio.update(objmuxio)              # update muxdata object 
                
    else:
        print ("test skipped.\n")
            
    print("hardware test finished.")


def playdemosound():
    subprocess.call("aplay ./user/audiofiles/demoaudio.wav", shell=True)
    
# function:  demo(arrcfg)
# show of all hardware functions
#    Input:  name of array containing hardware configuration
#    Output: -
def demo(objcfg): 
    # Initiate hardware first
    motor.init(motor, objcfg)
    #muxio.init(muxio, objcfg)
    objmuxio = muxio.muxiodata(objcfg)      # create mux data object
    funcmuxio = muxio.muxiofunc(objcfg)     # create mux control object
    
    
    playdemo = mp.Process(target=playdemosound, args=())
    playdemo.start()
    time.sleep(0.5)
    motor._set(motor, (1))
    while (True):
        subprocess.call("python3 ./lib/demoled.py", shell=True )