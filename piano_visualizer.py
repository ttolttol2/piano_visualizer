import time
from rpi_ws281x import PixelStrip, Color #sudo pip3 install rpi_ws281x
import mido

# LED strip configuration:
LED_COUNT = 144      # Number of LED pixels.
LED_PIN = 18         # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10         # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 10  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0      # set to '1' for GPIOs 13, 19, 41, 45 or 53


def read_midi_loop():
  #open midi port
  inport = mido.open_input('mio MIDI 1')
  while True:
    try:
        for msg in inport.iter_pending():
            note = msg.note
            if (msg.type == 'note_on'):
                velocity = msg.velocity
            elif (msg.type == 'note_off'):
                velocity = 0

            note_offset = 0
            #ledoff
            if(int(velocity) == 0 and int(note) > 0):
              strip.setPixelColor(((note - 28)*2 - note_offset), Color(0, 0, 0))
            #ledon
            elif(int(velocity) > 0 and int(note) > 0):
              #strip.setPixelColor(((note - 28)*2 - note_offset), Color(0, 0, 255))
              #strip.setPixelColor(((note - 28)*2 - note_offset), Color(197, 11, 226))
              #strip.setPixelColor(((note - 28)*2 - note_offset), Color(204, 0, 204))
              strip.setPixelColor(((note - 28)*2 - note_offset), Color(0, 255, 255))
            else:
              print("what else?")
        strip.show()

    except AttributeError as error:
        print("Error expected")
        pass

#Create NeoPixel object with appropriate configuration
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
#Intialize the library (must be called once before other functions).
strip.begin()

read_midi_loop()
