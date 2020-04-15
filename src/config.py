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

import configparser



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

# function:    read(arrcfg)
#     -     reads config file and saves variables into given array
#     Input:    arrcfg - name of array to save 
#    Output:    modifies input: arrcfg
def read(arrcfg):
    # create new Parser and read file
    config = configparser.ConfigParser()
    config.read('rpiloui.cfg')
    
    # Save values from file into given array
    # MAIN
    arrcfg.debug         = config['MAIN']['debug']
    
    #GAMESETTINGS
    arrcfg.game.tiltmaxtime        = int(config['GAMESETTINGS']['tiltmaxtime'])
    arrcfg.game.tiltrecovery    = int(config['GAMESETTINGS']['tiltmaxtime'])
    
    #CALIBRATION
    arrcfg.maxduty         = int(config['CALIBRATION']['maxduty'])
    arrcfg.pwmfreq        = int(config['CALIBRATION']['pwmfreq'])
    arrcfg.dirdeathtime = int(config['CALIBRATION']['dirdeathtime'])
    
    #PINMAPPING
    arrcfg.led_di         = int(config['PINMAPPING']['led-di'])
    arrcfg.led_ci         = int(config['PINMAPPING']['led-ci'])
    
    arrcfg.motor_cw     = int(config['PINMAPPING']['motor-cw'])
    arrcfg.motor_ccw     = int(config['PINMAPPING']['motor-ccw'])
    
    arrcfg.mux_coin        = int(config['PINMAPPING']['mux-coin'])
    arrcfg.mux_tilt        = int(config['PINMAPPING']['mux-tilt'])
    arrcfg.mux_action    = int(config['PINMAPPING']['mux-action'])
    
    arrcfg.mux[0]        = int(config['PINMAPPING']['mux-0'])
    arrcfg.mux[1]        = int(config['PINMAPPING']['mux-1'])
    arrcfg.mux[2]        = int(config['PINMAPPING']['mux-2'])
    arrcfg.mux[3]        = int(config['PINMAPPING']['mux-3'])
    arrcfg.mux[4]        = int(config['PINMAPPING']['mux-4'])
    arrcfg.mux[5]        = int(config['PINMAPPING']['mux-5'])
    arrcfg.mux[6]        = int(config['PINMAPPING']['mux-6'])
    arrcfg.mux[7]        = int(config['PINMAPPING']['mux-7'])
    
    #MUXMAPPING
    arrcfg.mapinput.coinsensor[0]    = int(config['MUXMAPPING']['coin0'])
    arrcfg.mapinput.coinsensor[1]    = int(config['MUXMAPPING']['coin1'])
    arrcfg.mapinput.coinsensor[2]    = int(config['MUXMAPPING']['coin2'])
    arrcfg.mapinput.coinsensor[3]    = int(config['MUXMAPPING']['coin3'])
    arrcfg.mapinput.coinsensor[4]    = int(config['MUXMAPPING']['coin4'])
    arrcfg.mapinput.coinsensor[5]    = int(config['MUXMAPPING']['coin5'])
    arrcfg.mapinput.coinsensor[6]    = int(config['MUXMAPPING']['coin6'])
    arrcfg.mapinput.coinsensor[7]    = int(config['MUXMAPPING']['coin7'])
    
    arrcfg.mapinput.tiltsensor[0]    = int(config['MUXMAPPING']['tilt0'])
    arrcfg.mapinput.tiltsensor[1]    = int(config['MUXMAPPING']['tilt1'])
    arrcfg.mapinput.tiltsensor[2]    = int(config['MUXMAPPING']['tilt2'])
    arrcfg.mapinput.tiltsensor[3]    = int(config['MUXMAPPING']['tilt3'])
    arrcfg.mapinput.tiltsensor[4]    = int(config['MUXMAPPING']['tilt4'])
    arrcfg.mapinput.tiltsensor[5]    = int(config['MUXMAPPING']['tilt5'])
    arrcfg.mapinput.tiltsensor[6]    = int(config['MUXMAPPING']['tilt6'])
    arrcfg.mapinput.tiltsensor[7]    = int(config['MUXMAPPING']['tilt7'])
    
    arrcfg.mapinput.actionbutton[0]    = int(config['MUXMAPPING']['action0'])
    arrcfg.mapinput.actionbutton[1]    = int(config['MUXMAPPING']['action1'])
    arrcfg.mapinput.actionbutton[2]    = int(config['MUXMAPPING']['action2'])
    arrcfg.mapinput.actionbutton[3]    = int(config['MUXMAPPING']['action3'])
    arrcfg.mapinput.actionbutton[4]    = int(config['MUXMAPPING']['action4'])
    arrcfg.mapinput.actionbutton[5]    = int(config['MUXMAPPING']['action5'])
    arrcfg.mapinput.actionbutton[6]    = int(config['MUXMAPPING']['action6'])
    arrcfg.mapinput.actionbutton[7]    = int(config['MUXMAPPING']['action7'])    


# function:    sanitize(arrcfg)
#     -    checks configuration variables for faulty values and correct them 
#          in order to prevent faulty game behavior or hardware damage 
#     Input:    name of array
#    Output:    -
def sanitize(arrcfg):
    
    if arrcfg.maxduty <= 1:
        arrcfg.maxduty = 1
    
    elif arrcfg.maxduty > 100:
        arrcfg.maxduty = 100
            
    if arrcfg.dirdeathtime < 1:
        arrcfg.dirdeathtime = 1
            
    elif arrcfg.dirdeathtime > 1000:
        arrcfg.dirdeathtime = 1000
        
    if arrcfg.game.tiltmaxtime < 1:
        arrcfg.game.tiltmaxtime = 1
    
    elif arrcfg.game.tiltmaxtime > 10:
        arrcfg.game.tiltmaxtime = 10
            
    if arrcfg.game.tiltrecover < 0.1:
        arrcfg.game.tiltrecover = 0.1
    
    elif arrcfg.game.tiltrecover > 10:
        arrcfg.game.tiltrecover = 10


    