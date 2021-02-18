#!/usr/bin/python
# Python script to convert epub format to mobi
# wrote by kovidgoyal https://www.mobileread.com/forums/showthread.php?t=179686
# Can process more than 1 book per time
import os, time, glob, subprocess

files = glob.glob('*.epub')

workers = []
while files or workers:
    while len(workers) < 4 and files:
        f = files[0]
        files = files[1:]
        w = subprocess.Popen(['ebook-convert', f,
            os.path.splitext(f)[0]+'.mobi'])
        workers.append(w)
    for w in list(workers):
        if w.poll() is not None:
            workers.remove(w)
    time.sleep(0.1)
