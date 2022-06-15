#!/bin/env python3
"""
    Example program to output an animated face
    to a file or set of files.
"""

import time
from pathlib import PurePath

import face

ani_upd_per = 1.0 # seconds
outfile = "./out/face.png"
# If set to True, a counter will be added to the filename.
# This can be used to create an animation from the outputted
# set of files.
append_counter = False
# Initial value for file counter
counter = 0

# Create face object
face = face.Face()

try:
    print("Press Ctrl+c to exit.")
    while True:
        # Time at start of loop
        t0 = time.time()

        # Update face frame
        face.update()

        # Output face frame to file
        if True==append_counter:
            c_outfile = str(PurePath(outfile).parent) + "/" +             str(PurePath(outfile).stem) + "_" + str(counter).rjust(8, "0")n+ str(PurePath(outfile).suffix)
            counter += 1
        else:
            c_outfile = outfile

        face.frame.save(c_outfile)

        # Wait until update period has passed
        dt = ani_upd_per - (time.time() - t0)
        if dt > 0:
            time.sleep(dt)

except KeyboardInterrupt:
    print("Exiting loop.")
    exit
