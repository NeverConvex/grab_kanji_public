:: This is a simple Windows batch script. It runs win_screenshot2.py to generate an image from a target monitor(s),
:: and then runs google_ocr to extract Japanese text from the image generated from that monitor.

:: In the original configuration, python.exe was a full path to a Windows-installed copy of Python with a functional copy of
:: the mss library
python.exe win_screenshot.py
:: In the original configuration, python was a full path to a copy of python running inside Ubuntu installed in Windows Linux as a
:: Subsystem
wsl.exe python google_ocr.py
:: Use of both WSL and Windows copies of Python is a bit annoying -- one for MSS, one for Google OCR -- but with this Windows batch script we can run one before the other. (Side note: more modern versions of WSL make use of MSS easy there as well, the original motivation for this workaround.)
