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

import array
import binascii
import configparser
import datetime
import io
import logging
import os
import sys
import time

try:
	import serial
except ImportError:
	pass


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
	#arrcfg.samplevariable = config['MAIN']['samplevariable']

	return
	