piano_visualizer
================
only very simple functions which light on when key is pressed operate.    
see this [site](https://github.com/onlaj/Piano-LED-Visualizer) for details of system.   
![piano_led](https://user-images.githubusercontent.com/2408306/76138407-13f89400-608b-11ea-8901-a6d83f9ee136.png)

## what you needs
### 1) Hardware:
* piano with MIDI (veloce SE-120N)
* raspberry pi (3 b+)
* MIDI to USB interface(iConnectivity mio)
* WS2812B LED Strip (1m with 144 diodes/meter)
* Power Supply (5V 4A, 6A is enough to light 172 LEDs @50% power)
* Some wires
### 2) Software:
* raspbian
* ssh (to change LED brightness and color)
* python & python library(rpi_ws281x, mido)
* piano_visualizer.py

## LED strip wiring
https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring
* Pi pin 18 to NeoPixel DIN.
* 1N4001 diode cathode (side with the stripe) to NeoPixel 5V.
* Power supply ground to Pi ground.
* Power supply ground to NeoPixel GND.
* Power supply 5V to 1N4001 diode anode (side without the stripe).
![Alt text](https://cdn-learn.adafruit.com/assets/assets/000/064/122/medium640/led_strips_raspi_NeoPixel_Diode_bb.jpg?1540315941)
