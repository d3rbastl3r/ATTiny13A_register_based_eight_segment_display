#!/usr/bin/python3

import os
import sys

from pathlib import Path

MCU_NAME = "t13"
ISP_NAME = "avrisp2"
HEX_FILE_NAME = "ATTiny13A_register_based_eight_segment_display.hex"

if not MCU_NAME:
    print("MCU_NAME is not set")
    sys.exit()
	
if not ISP_NAME:
    print("ISP_NAME is not set")
    sys.exit()
	
if not HEX_FILE_NAME:
    print("HEX_FILE_NAME is not set")
    sys.exit()

hexFile = Path("./bin/Release/" + HEX_FILE_NAME)
if not hexFile.exists():
    print("File './bin/Release/" + HEX_FILE_NAME + "' does not exists")
    sys.exit()

os.system("avrdude -p " + MCU_NAME + " -c " + ISP_NAME + " -P usb -U flash:w:./bin/Release/" + HEX_FILE_NAME)
