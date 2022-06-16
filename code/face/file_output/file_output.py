"""
    Example program to output an animated face
    to a file or series of files.
"""

import time
from threading import Thread
from pathlib import PurePath

import face

ani_run = False
ani_upd_per = 1.0 # seconds
outfile = "./out/face.png"
# If append_counter is set to true an automatically incremented counter
# will be added to the output file. This way, the series of files can be
# used to create a small video/animation. If set to false, the same file
# will be overwritten for every frame. An image viewer can be used to
# have a "live view" on the file and follow the animation.
append_counter = False

# Create face object
face = face.Face()

def ani_thread():
    # Initialize counter - may be used later
    counter = 0
    while ani_run:
        # Time at start of loop
        t0 = time.time()

        # Update face frame
        face.update()

        # Output face frame to file
        if append_counter:
            c_outfile = str(PurePath(outfile).parent) + "/" + str(PurePath(outfile).stem) + "_" + str(counter).rjust(8, "0") + str(PurePath(outfile).suffix)
            # Increment counter
            counter += 1
        else:
            c_outfile = outfile
        face.frame.save(c_outfile)

        # Wait until update period has passed
        dt = ani_upd_per - (time.time() - t0)
        if dt > 0:
            time.sleep(dt)

def animate(stop = False):
    global ani_run

    if stop:
        ani_run = False
    else:
        if not ani_run:
            ani_run = True
            a = Thread(target=ani_thread, daemon=True)
            a.start()


