"""
simple test program that led on when the key is pressed and off when the key is released.
"""
import mido
import time
from datetime import timedelta
from rpi_ws281x import PixelStrip, Color #sudo pip3 install rpi_ws281x

# LED strip configuration:
LED_COUNT = 144      # Number of LED pixels.
LED_PIN = 18         # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10         # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 200 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0      # set to '1' for GPIOs 13, 19, 41, 45 or 53


def read_midi():
    inport = mido.open_input('mio MIDI 1') #change to your device file
    while True:
        try:
            start = time.time()
            for msg in inport.iter_pending():
                if (msg.type == 'note_on' and msg.velocity > 0):
                    end = time.time()
                    print(msg.note, 'on', timedelta(seconds=end-start))
                    strip.setPixelColor(68, Color(255, 0, 0))
                else:
                    end = time.time()
                    print(msg.note, 'off', timedelta(seconds=end-start))
                    strip.setPixelColor(68, Color(0, 0, 0))
            strip.show()

        except AttributeError as error:
            print("Error expected")
            pass

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

read_midi()
