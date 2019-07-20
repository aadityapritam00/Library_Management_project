import time
import sys

def loading_view(): 
    toolbar_width = 60 
    # setup toolbar
    sys.stdout.write("[%s]" % ("" * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
    print("Loading")
    for i in range(toolbar_width):
        time.sleep(0.1) 
        sys.stdout.write(".")
        sys.stdout.flush()
    sys.stdout.write(" \n") 