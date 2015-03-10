from Tkinter import Tk
from tkFileDialog import askdirectory

import os
import sys

if len(sys.argv) < 2:
	Tk().withdraw()
	path = askdirectory()
else:
	path = sys.argv[1]

try:
	for f in os.listdir(path):
		if os.path.isfile(os.path.join(path, f)):
			os.rename(os.path.join(path, f), os.path.join(path, f.lower()))
	print "Renamed files in " + path + " to lowercase"
except OSError, e:
	print e
