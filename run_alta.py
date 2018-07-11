#!/usr/bin/env python2.7

# APERTIF HAPPILI > ALTA SCRIPT RUNNER (run_alta.py)
# V.A. Moss 11/07/2018 (vmoss.astro@gmail.com)
__author__ = "V.A. Moss"
__date__ = "$11-jul-2018 12:00:00$"
__version__ = "1.0"

import os
import sys

path = '../transfer/'

# Get list of possible datasets
datasets = []
cmd = os.popen('ls -d %s/*' % path)
for x in cmd:
	folder = x.strip()
	datasets.append(folder)

print datasets

sys.exit()
