################################################################################
#
# rpiloui - a python game engine for hasbros looping loui game controlled via a
#           raspberry pi single board computer
#
# This code is released under: 
#
# Copyright (c) 2020 nasrudin2468
#
# TODO: licence text
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


################################################################################
# Functions

# function:	read(message)
# 	-
# 	Input:	name of array
#	Output:	modifies input
def read(arrcfg):
	# create new Parser and read file
	config = configparser.ConfigParser()
	config.read('rpiloui.cfg')
	
	# Save values from file into given array
	# MAIN
	arrcfg.debug 		= config['MAIN']['debug']
	
	#GAMESETTINGS
	# -
	
	#CALIBRATION
	arrcfg.maxduty 		= config['CALIBRATION']['maxduty']
	arrcfg.dirdeathtime = config['CALIBRATION']['dirdeathtime']
	
	#PINMAPPING
	arrcfg.led_di 		= config['PINMAPPING']['led-di']
	arrcfg.led_ci 		= config['PINMAPPING']['led-ci']
	
	arrcfg.motor_cw 	= config['PINMAPPING']['motor-cw']
	arrcfg.motor_ccw 	= config['PINMAPPING']['motor-ccw']
	
	arrcfg.mux_0		= config['PINMAPPING']['mux-0']
	arrcfg.mux_1		= config['PINMAPPING']['mux-1']
	arrcfg.mux_2		= config['PINMAPPING']['mux-2']
	arrcfg.mux_3		= config['PINMAPPING']['mux-3']
	arrcfg.mux_4		= config['PINMAPPING']['mux-4']
	arrcfg.mux_5		= config['PINMAPPING']['mux-5']
	arrcfg.mux_6		= config['PINMAPPING']['mux-6']
	arrcfg.mux_7		= config['PINMAPPING']['mux-7']
	
	arrcfg.mux_coin		= config['PINMAPPING']['mux-coin']
	arrcfg.mux_tilt		= config['PINMAPPING']['mux-tilt']
	arrcfg.mux_action	= config['PINMAPPING']['mux-action']
	