import numpy as np
#from pymouse import PyMouse
from PIL import Image, ImageChops
import mss, time, os, pathlib#, glob, fire
#from fpdf import FPDF
#from copy import deepcopy

"""
Grabs a simple screenshot from a target monitor(s). Meant to be used in conjunction with google_ocr.py, to first take a screenshot
of an actively running game or program, then extract text from it and display it for the user to copy/paste as they wish.

A complication is that win_screen uses mss, which we only know how to run from Windows, while google_ocr uses the Google Vision
libraries, which we only know how to run from WSL.
"""

ss_size = (3840, 2160)
mssi = mss.mss()

def test(monitors=[0]): # 0 = both screens, 1 = first monitor, 2 = second monitor
    cwd = os.getcwd()
    for mnum in monitors:
        ss = mssi.grab(mssi.monitors[mnum])
        img = Image.frombytes("RGB", ss.size, ss.bgra, "raw", "BGRX")
        img.save(cwd + f"\\test\\test{mnum}.png", "PNG", **{})

if __name__ == "__main__":
    test()
