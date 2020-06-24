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

from . import motor
from . import muxio
from . import config


# Prevent direct access to this file since it would be useless
if __name__ == '__main__':
    exit()


################################################################################
# Functions


def pmuxio(pipe):
# function: pmuxio(pipe)
# subprocess target function for scanning and analyzing mux input state
#    Input:  data pipe object (defined on creation of subprocess)
#    Output: -
    
    #create local data object by receive copy from pipe
    objmuxio = pipe.recv()
    
    funcmuxio = muxio.muxiofunc(config.objconfig())   # create mux control object
    
    while (True):
        muxio.poll(objmuxio, funcmuxio)     # poll actual muxdata (currentstate)
        pipe.send(objmuxio.currentstate)    # pipe it to main process
        time.sleep(0.05)                    # wait for next scan cycle


# function: start()
# Initiate Game by calling hardware inits and pass over to the game statemachine 
#    Input:  name of array containing configuration data
#    Output: -
def start(objcfg):
    random.seed(a=None, version=2)          # Initiate random number generator
    
    objmuxio = muxio.muxiodata(objcfg)      # Create muxdata object
    parent_muxio, child_muxio = mp.Pipe()   # Create pipe for mux data exchange
                                            # between main process and mux
                                            # hardware scan process
    motor.init(motor, objcfg)               # Initiate motor hardware and create
                                            # motor data object
    
    # create game logic data list
    game = type('', (), {})
    game.state = 0
    game.playercoins = [3] * 8
    game.looser = 0
    game.state = 0

    # send mux data object first time for object creation within child process
    parent_muxio.send(objmuxio)            
    
    # define child process processmuxio, define pmuxio as target function and
    # child_muxio as argument
    processmuxio = mp.Process(target=pmuxio, args=(child_muxio,))
    
    processmuxio.start()                    # start process
    print ("STM: Start")

    #muxio.update(objmuxio)                  # Update to inital state since different actors have different Idle states

    while (True):
        statemachine(parent_muxio, motor, objmuxio, game)


def statemachine(pipeobject, objmotor, objmuxio, game):
    if game.state == 0:
        if pipeobject.poll() == True:
            objmuxio.currentstate = pipeobject.recv()
            for i in range(0, 8 , 1):
                if (muxio.waschanged(objmuxio, BUTTON, RELEASED, i) == True):
                    game.state = 1
                    print ("STM: Reset!")
            muxio.update(objmuxio)
    
    elif game.state == 1:
        game.playercoins = [3,3,3,3,3,3,3,3]    # Reset Coin Counters
        motor._set(objmotor, 0.5)               # Start Motor
        game.state = STMRUN                     # Switch to RUN
        print ("STM: RUN")
        muxio.update(objmuxio)
    
    elif game.state == 2:
        # Check individual coin counters
        if pipeobject.poll() == True:
            objmuxio.currentstate = (pipeobject.recv())
            for i in range(0, 8 , 1):
                if (muxio.waschanged(objmuxio, COIN, VANISHED, i) == True):
                    game.playercoins[i] -= 1
                    print ("player", i, "coins left", game.playercoins[i])  
            muxio.update(objmuxio)
        
        # Goto stop if looser is detected
        for i in range(0, 8, 1):
            if (game.playercoins[i] < 1):
                game.looser = i
                game.state = 3
                print ("STM: Stop")
                print ("player",game.looser,"lost this round. Cheers!")
       
    
    elif game.state == 3:
        motor._set(objmotor, 0)   # Stop motor
        # TODO: looser animation
        # switch to reset if looser button is activated
        if pipeobject.poll() == True:
            objmuxio.currentstate = (pipeobject.recv())
            for i in range(0, 8 , 1):
                if (muxio.waschanged(objmuxio, BUTTON, RELEASED, i) == True):
                    print ("STM: Reset!")
                    game.state = 1
            muxio.update(objmuxio)
    


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
    
    
    