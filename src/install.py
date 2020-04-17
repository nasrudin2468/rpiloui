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
import sys


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

# function: install()
# Installs dependencies required for rpiloui using pip interface 
#    Input:  -
#    Output: -
def install():
    print("Install required libraries. Requires internet connection! Might need admin / root...")

    print("Installing pyserial via pip... ")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyserial"])
    print("Installing gpiozero via pip... ")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gpiozero"])            
    print("Installing apa102-pi via pip... ")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "apa102-pi"])
    

        