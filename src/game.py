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

import multiprocessing  as mp
import random
import time


################################################################################
# Constants

STMSTART    = 0
STMRESET    = 1
STMRUN      = 2
STMSTOP     = 3

COIN        = 0
TILT        = 1
BUTTON      = 2

RELEASED    = 0
DETECTED    = 0
VANISHED    = 1
PRESSED     = 1




################################################################################
# classes / structs


################################################################################
# Import external functions


# Prevent direct access to this file since it would be useless
if __name__ == '__main__':
    exit()


################################################################################
# Functions

# function: start()
# Initiate Game by calling hardware inits and pass over to the game statemachine 
#    Input:  name of array containing configuration data
#    Output: -
def start(arrcfg):
    random.seed(a=None, version=2)  #    Initiate random number generator
    
    while (True):
        statemachine()


def statemachine():
    pass    


'''
Sketch: basic game concept

1. Startup state
    show start animation
    switch to 2 on press of any key
2. select Active players menu
    switch to 3 after specific time
3. start game on press of any key
4. Reset Coin counter
5. Start Motor
    Decrease coin counter of each player if decrease is detected
    switch to 6 if first counter reaches zero
    switch to 6 if first tilt limit exceeded
6. Stop  Motor. Show Loose Animation
    switch to 1 if two tilts are activated more than double tilt time
    switch to 7 after double tilt time
7. Reset Loose State: switch to 2 on button press and release of Looser

'''
    
    
    