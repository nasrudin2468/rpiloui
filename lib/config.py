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

# function:	read(arrcfg)
# 	- 	reads config file and saves variables into given array
# 	Input:	name of array to save 
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
	arrcfg.maxduty 		= int(config['CALIBRATION']['maxduty'])
	arrcfg.pwmfreq		= int(config['CALIBRATION']['pwmfreq'])
	arrcfg.dirdeathtime = int(config['CALIBRATION']['dirdeathtime'])
	
	#PINMAPPING
	arrcfg.led_di 		= int(config['PINMAPPING']['led-di'])
	arrcfg.led_ci 		= int(config['PINMAPPING']['led-ci'])
	
	arrcfg.motor_cw 	= int(config['PINMAPPING']['motor-cw'])
	arrcfg.motor_ccw 	= int(config['PINMAPPING']['motor-ccw'])
	
	arrcfg.mux_0		= int(config['PINMAPPING']['mux-0'])
	arrcfg.mux_1		= int(config['PINMAPPING']['mux-1'])
	arrcfg.mux_2		= int(config['PINMAPPING']['mux-2'])
	arrcfg.mux_3		= int(config['PINMAPPING']['mux-3'])
	arrcfg.mux_4		= int(config['PINMAPPING']['mux-4'])
	arrcfg.mux_5		= int(config['PINMAPPING']['mux-5'])
	arrcfg.mux_6		= int(config['PINMAPPING']['mux-6'])
	arrcfg.mux_7		= int(config['PINMAPPING']['mux-7'])
	
	arrcfg.mux_coin		= int(config['PINMAPPING']['mux-coin'])
	arrcfg.mux_tilt		= int(config['PINMAPPING']['mux-tilt'])
	arrcfg.mux_action	= int(config['PINMAPPING']['mux-action'])
	return

# function:	sanitize(arrcfg)
# 	-	checks array variables for faulty values and abort program
#	  	in order to prevent hardware damage
# 	Input:	name of array
#	Output:	modifies input
def sanitize(arrcfg):
	
	if arrcfg.maxduty <= 1:
			arrcfg.maxduty = 1
	
	if arrcfg.maxduty > 100:
			arrcfg.maxduty = 100
			
	if arrcfg.dirdeathtime < 1:
			arrcfg.dirdeathtime = 1
			
	if arrcfg.dirdeathtime > 1000:
			arrcfg.dirdeathtime = 1000
			
	return
	