""" 
simple test program that displays on when the key is pressed and off when the key is released. 
"""
import mido
import time
from datetime import timedelta

def read_midi():
    inport = mido.open_input('mio MIDI 1') #change to your device file
    while True:
        try:
            start = time.time()
            for msg in inport.iter_pending():
                if (msg.type == 'note_on' and msg.velocity > 0):
                    end = time.time()
                    print(msg.note, 'on', timedelta(seconds=end-start).microseconds)
                else:
                    end = time.time()
                    print(msg.note, 'off', timedelta(seconds=end-start).microseconds)

        except AttributeError as error:
            print("Error expected")
            pass
read_midi()
