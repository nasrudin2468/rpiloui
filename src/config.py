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

class objgame:
    def __init__(self):
        # create new Parser and read file
        config = configparser.ConfigParser()
        config.read('rpiloui.cfg')

        self.tiltmaxtime     = int(config['GAMESETTINGS']['tiltmaxtime'])
        self.tiltrecovery    = float(config['GAMESETTINGS']['tiltrecovery'])
        
class objmux:
    def __init__(self):
        # create new Parser and read file
        config = configparser.ConfigParser()
        config.read('rpiloui.cfg')
        
        self.input      = [None] * 8
        self.input[0] = int(config['PINMAPPING']['mux-0'])
        self.input[1] = int(config['PINMAPPING']['mux-1'])
        self.input[2] = int(config['PINMAPPING']['mux-2'])
        self.input[3] = int(config['PINMAPPING']['mux-3'])
        self.input[4] = int(config['PINMAPPING']['mux-4'])
        self.input[5] = int(config['PINMAPPING']['mux-5'])
        self.input[6] = int(config['PINMAPPING']['mux-6'])
        self.input[7] = int(config['PINMAPPING']['mux-7'])

class objmapinput:
    def __init__(self):
        # create new Parser and read file
        config = configparser.ConfigParser()
        config.read('rpiloui.cfg')
        
        self.coinsensor      = [None] * 8
        self.coinsensor[0]   = int(config['MUXMAPPING']['coin0'])
        self.coinsensor[1]   = int(config['MUXMAPPING']['coin1'])
        self.coinsensor[2]   = int(config['MUXMAPPING']['coin2'])
        self.coinsensor[3]   = int(config['MUXMAPPING']['coin3'])
        self.coinsensor[4]   = int(config['MUXMAPPING']['coin4'])
        self.coinsensor[5]   = int(config['MUXMAPPING']['coin5'])
        self.coinsensor[6]   = int(config['MUXMAPPING']['coin6'])
        self.coinsensor[7]   = int(config['MUXMAPPING']['coin7'])
    
        self.tiltsensor      = [None] * 8
        self.tiltsensor[0]   = int(config['MUXMAPPING']['tilt0'])
        self.tiltsensor[1]   = int(config['MUXMAPPING']['tilt1'])
        self.tiltsensor[2]   = int(config['MUXMAPPING']['tilt2'])
        self.tiltsensor[3]   = int(config['MUXMAPPING']['tilt3'])
        self.tiltsensor[4]   = int(config['MUXMAPPING']['tilt4'])
        self.tiltsensor[5]   = int(config['MUXMAPPING']['tilt5'])
        self.tiltsensor[6]   = int(config['MUXMAPPING']['tilt6'])
        self.tiltsensor[7]   = int(config['MUXMAPPING']['tilt7'])
    
        self.actionbutton    = [None] * 8
        self.actionbutton[0] = int(config['MUXMAPPING']['action0'])
        self.actionbutton[1] = int(config['MUXMAPPING']['action1'])
        self.actionbutton[2] = int(config['MUXMAPPING']['action2'])
        self.actionbutton[3] = int(config['MUXMAPPING']['action3'])
        self.actionbutton[4] = int(config['MUXMAPPING']['action4'])
        self.actionbutton[5] = int(config['MUXMAPPING']['action5'])
        self.actionbutton[6] = int(config['MUXMAPPING']['action6'])
        self.actionbutton[7] = int(config['MUXMAPPING']['action7']) 
        
class objconfig:
    def __init__(self):
        # create new Parser and read file
        config = configparser.ConfigParser()
        config.read('rpiloui.cfg')
    
        # Save values from file into given array
        # MAIN
        self.debug        = config['MAIN']['debug']
    
        #GAMESETTINGS
        self.game                 = objgame()
    
        #CALIBRATION
        self.maxduty      = int(config['CALIBRATION']['maxduty'])
        self.pwmfreq      = int(config['CALIBRATION']['pwmfreq'])
        self.dirdeathtime = int(config['CALIBRATION']['dirdeathtime'])
    
        #PINMAPPING
        self.led_di       = int(config['PINMAPPING']['led-di'])
        self.led_ci       = int(config['PINMAPPING']['led-ci'])
    
        self.motor_cw     = int(config['PINMAPPING']['motor-cw'])
        self.motor_ccw    = int(config['PINMAPPING']['motor-ccw'])
        self.mux_coin     = int(config['PINMAPPING']['mux-coin'])
        self.mux_tilt     = int(config['PINMAPPING']['mux-tilt'])
        self.mux_action   = int(config['PINMAPPING']['mux-action'])
        
        self.mux          = objmux()
    
        #MUXMAPPING
        self.mapinput          = objmapinput()
    
        
    
# function:    read(objcfg)
#     -     reads config file and saves variables into given array
#     Input:    objcfg - name of object which will hold save data
#    Output:    modifies input: objcfg
def read(objcfg):
    # create new Parser and read file
    config = configparser.ConfigParser()
    config.read('rpiloui.cfg')
    
    # Save values from file into given array
    # MAIN
    objcfg.debug        = config['MAIN']['debug']
    
    #GAMESETTINGS
    objcfg.game                 = type('', (), {})
    objcfg.game.tiltmaxtime     = int(config['GAMESETTINGS']['tiltmaxtime'])
    objcfg.game.tiltrecovery    = float(config['GAMESETTINGS']['tiltrecovery'])
    
    #CALIBRATION
    objcfg.maxduty      = int(config['CALIBRATION']['maxduty'])
    objcfg.pwmfreq      = int(config['CALIBRATION']['pwmfreq'])
    objcfg.dirdeathtime = int(config['CALIBRATION']['dirdeathtime'])
    
    #PINMAPPING
    objcfg.led_di       = int(config['PINMAPPING']['led-di'])
    objcfg.led_ci       = int(config['PINMAPPING']['led-ci'])
    
    objcfg.motor_cw     = int(config['PINMAPPING']['motor-cw'])
    objcfg.motor_ccw    = int(config['PINMAPPING']['motor-ccw'])
    objcfg.mux          = type('', (), {})
    objcfg.mux_coin     = int(config['PINMAPPING']['mux-coin'])
    objcfg.mux_tilt     = int(config['PINMAPPING']['mux-tilt'])
    objcfg.mux_action   = int(config['PINMAPPING']['mux-action'])
    objcfg.mux.input    = [None] * 8
    objcfg.mux.input[0] = int(config['PINMAPPING']['mux-0'])
    objcfg.mux.input[1] = int(config['PINMAPPING']['mux-1'])
    objcfg.mux.input[2] = int(config['PINMAPPING']['mux-2'])
    objcfg.mux.input[3] = int(config['PINMAPPING']['mux-3'])
    objcfg.mux.input[4] = int(config['PINMAPPING']['mux-4'])
    objcfg.mux.input[5] = int(config['PINMAPPING']['mux-5'])
    objcfg.mux.input[6] = int(config['PINMAPPING']['mux-6'])
    objcfg.mux.input[7] = int(config['PINMAPPING']['mux-7'])
    
    #MUXMAPPING
    objcfg.mapinput                 = type('', (), {})
    objcfg.mapinput.coinsensor      = [None] * 8
    objcfg.mapinput.coinsensor[0]   = int(config['MUXMAPPING']['coin0'])
    objcfg.mapinput.coinsensor[1]   = int(config['MUXMAPPING']['coin1'])
    objcfg.mapinput.coinsensor[2]   = int(config['MUXMAPPING']['coin2'])
    objcfg.mapinput.coinsensor[3]   = int(config['MUXMAPPING']['coin3'])
    objcfg.mapinput.coinsensor[4]   = int(config['MUXMAPPING']['coin4'])
    objcfg.mapinput.coinsensor[5]   = int(config['MUXMAPPING']['coin5'])
    objcfg.mapinput.coinsensor[6]   = int(config['MUXMAPPING']['coin6'])
    objcfg.mapinput.coinsensor[7]   = int(config['MUXMAPPING']['coin7'])
    
    objcfg.mapinput.tiltsensor      = [None] * 8
    objcfg.mapinput.tiltsensor[0]   = int(config['MUXMAPPING']['tilt0'])
    objcfg.mapinput.tiltsensor[1]   = int(config['MUXMAPPING']['tilt1'])
    objcfg.mapinput.tiltsensor[2]   = int(config['MUXMAPPING']['tilt2'])
    objcfg.mapinput.tiltsensor[3]   = int(config['MUXMAPPING']['tilt3'])
    objcfg.mapinput.tiltsensor[4]   = int(config['MUXMAPPING']['tilt4'])
    objcfg.mapinput.tiltsensor[5]   = int(config['MUXMAPPING']['tilt5'])
    objcfg.mapinput.tiltsensor[6]   = int(config['MUXMAPPING']['tilt6'])
    objcfg.mapinput.tiltsensor[7]   = int(config['MUXMAPPING']['tilt7'])
    
    objcfg.mapinput.actionbutton    = [None] * 8
    objcfg.mapinput.actionbutton[0] = int(config['MUXMAPPING']['action0'])
    objcfg.mapinput.actionbutton[1] = int(config['MUXMAPPING']['action1'])
    objcfg.mapinput.actionbutton[2] = int(config['MUXMAPPING']['action2'])
    objcfg.mapinput.actionbutton[3] = int(config['MUXMAPPING']['action3'])
    objcfg.mapinput.actionbutton[4] = int(config['MUXMAPPING']['action4'])
    objcfg.mapinput.actionbutton[5] = int(config['MUXMAPPING']['action5'])
    objcfg.mapinput.actionbutton[6] = int(config['MUXMAPPING']['action6'])
    objcfg.mapinput.actionbutton[7] = int(config['MUXMAPPING']['action7'])    


# function:    sanitize(objcfg)
#     -    checks configuration variables for faulty values and correct them 
#          in order to prevent faulty game behavior or hardware damage 
#     Input:    name of object holding config data
#    Output:    -
def sanitize(objcfg):
    
    if objcfg.maxduty <= 1:
        objcfg.maxduty = 1
    
    elif objcfg.maxduty > 100:
        objcfg.maxduty = 100
            
    if objcfg.dirdeathtime < 1:
        objcfg.dirdeathtime = 1
            
    elif objcfg.dirdeathtime > 1000:
        objcfg.dirdeathtime = 1000
        
    if objcfg.game.tiltmaxtime < 1:
        objcfg.game.tiltmaxtime = 1
    
    elif objcfg.game.tiltmaxtime > 10:
        objcfg.game.tiltmaxtime = 10
            
    if objcfg.game.tiltrecovery < 0.1:
        objcfg.game.tiltrecovery = 0.1
    
    elif objcfg.game.tiltrecovery > 10:
        objcfg.game.tiltrecovery = 10


    