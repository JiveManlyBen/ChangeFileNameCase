from tkinter import *
from tkinter import filedialog

import os
import sys

if len(sys.argv) < 2:
	path = filedialog.askdirectory()
else:
	path = sys.argv[1]

try:
	for f in os.listdir(path):
		if os.path.isfile(os.path.join(path, f)):
			os.rename(os.path.join(path, f), os.path.join(path, f.lower()))
	print("Renamed files in " + path + " to lowercase")
except OSError as e:
	print(e)
