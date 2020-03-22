""" 
simple test program that displays on when the key is pressed and off when the key is released. 
"""
import mido

def read_midi():
    inport = mido.open_input('mio MIDI 1') #change to your device file
    while True:
        try:
            for msg in inport.iter_pending():
                if (msg.type == 'note_on'):
                    print(msg.note, 'on')
                elif (msg.type == 'note_off'):
                    print(msg.note, 'off')

        except AttributeError as error:
            print("Error expected")
            pass
read_midi()
