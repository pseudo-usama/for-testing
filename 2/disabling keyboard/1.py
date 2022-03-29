# https://stackoverflow.com/questions/29289945/how-to-temporarily-disable-keyboard-input-using-python


import time
class keyboardDisable():

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def __call__(self): 
        while self.on:
            msvcrt.getwch()


    def __init__(self):
        self.on = False
        import msvcrt

disable = keyboardDisable()
disable.start()
time.sleep(10)
disable.stop()