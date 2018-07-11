#!/usr/bin/env python2.7

# APERTIF HAPPILI > ALTA SCRIPT RUNNER (run_alta.py)
# V.A. Moss 11/07/2018 (vmoss.astro@gmail.com)
__author__ = "V.A. Moss"
__date__ = "$11-jul-2018 12:00:00$"
__version__ = "1.0"

import os
import sys

path = '../transfer'

# Get list of possible datasets
datasets = []
cmd = os.popen('ls -d %s/*' % path)
for x in cmd:
	folder = x.strip()
	datasets.append(folder)

for ds in datasets:

	# run from within the folder
	os.chdir('%s' % ds)

	# Run the transfer script
	print 'Running script for %s...' % ds
	os.system('./transfer_all.sh')

	# Change back to code directory
	os.chdir('../../push2alta/')

	# Move the folder to "done"
	os.system('mv %s ../done/' % ds)