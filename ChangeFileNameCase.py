import os
import sys

path = sys.argv[1]

try:
	for f in os.listdir(path):
		if os.path.isfile(os.path.join(path, f)):
			os.rename(os.path.join(path, f), os.path.join(path, f.lower()))
	print "Renamed files in " + path + " to lowercase"
except OSError, e:
	print e
