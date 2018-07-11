#!/usr/bin/env python2.7

# APERTIF PARSET GENERATOR (apgen.py)
# Input: source text file
# V.A. Moss 05/04/2018 (vmoss.astro@gmail.com)
__author__ = "V.A. Moss"
__date__ = "$05-apr-2018 16:00:00$"
__version__ = "1.0"

import os
import sys

path = '/data/apertif'
maxdate = 180126

# Get list of possible datasets
datasets = []
cmd = os.popen('du -sh %s/1*' % path)
for x in cmd:
	col = x.split()
	size = col[0]
	folder = col[1]
	if size != '0':
		datasets.append(folder)

for ds in datasets:

	tid = ds.split('/')[-1].split('_')[0]
	date = float(tid[0:6])
	
	# Consider only the dataset before a certain date
	if date <= maxdate:

		# Assume it is not in ALTA or will be dealt with at a later stage...
		os.system('mkdir ../transfer/WSRTA%s' % tid)
		os.chdir('../transfer/WSRTA%s' % tid)
		os.system("../prepare_transfer_alta.sh -s /data/apertif/%s -f '.*%s.*' -i 'icat,res1' -1" % (ds,tid))

		sys.exit()
	


