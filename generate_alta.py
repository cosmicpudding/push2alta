#!/usr/bin/env python2.7

# APERTIF HAPPILI > ALTA SCRIPT GENERATOR (generate_alta.py)
# Input: path, maximum date to consider
# V.A. Moss 11/07/2018 (vmoss.astro@gmail.com)
__author__ = "V.A. Moss"
__date__ = "$11-jul-2018 12:00:00$"
__version__ = "1.0"

import os
import sys

path = '/data/apertif'
maxdate = 180126

# Get list of possible datasets
print 'Getting list of datasets...'
datasets = []
cmd = os.popen('du -sh %s/1*' % path)
for x in cmd:
	col = x.split()
	size = col[0]
	folder = col[1]
	if size != '0':
		datasets.append(folder)

print 'Looping through datasets to create scripts...'
for ds in datasets:

	print ds

	tid = ds.split('/')[-1].split('_')[0]
	date = float(tid[0:6])
	
	# Consider only the dataset before a certain date
	if date <= maxdate:

		# Assume it is not in ALTA or will be dealt with at a later stage...
		os.system('mkdir ../transfer/WSRTA%s' % tid)
		os.chdir('../transfer/WSRTA%s' % tid)
		os.system("../../prepare_transfer_alta.sh -s %s -f '.*%s.*' -i 'icat,res1,res2,res3' -1" % (ds,tid))
		
		# Change back to original directory
		os.chdir('../../push2alta/')


