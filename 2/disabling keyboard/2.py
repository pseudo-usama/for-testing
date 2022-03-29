# https://stackoverflow.com/questions/29289945/how-to-temporarily-disable-keyboard-input-using-python


import sys
import time


stdout = sys.stdout
sys.stdout = sys.stderr
time.sleep(2)

sys.stdout = stdout

while True:
    pass
