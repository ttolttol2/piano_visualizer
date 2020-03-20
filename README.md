piano_visualizer
================
only very simple functions which light on when key is pressed operate.    
see this [site](https://github.com/onlaj/Piano-LED-Visualizer) for details of system.   
![piano_led](https://user-images.githubusercontent.com/2408306/76138407-13f89400-608b-11ea-8901-a6d83f9ee136.png)
(https://youtu.be/87CoHgi19pU)

## what you needs
### 1) Hardware:
* piano with MIDI (veloce SE-120N)
* raspberry pi (3 b+)
* MIDI to USB interface(iConnectivity mio)
* WS2812B LED Strip (1m with 144 diodes/meter)
* Power Supply (5V 4A, 6A is enough to light 172 LEDs @50% power)
* Some wires   
![wiring](https://user-images.githubusercontent.com/2408306/76139039-f4179f00-608f-11ea-9ecd-d1046e7bb37f.png)
### 2) Software:
* raspbian
* ssh (to change LED brightness and color)
* python & python library(rpi_ws281x, mido)
* piano_visualizer.py
``` 
pi@raspberrypi:~ $ uname -a
Linux raspberrypi 4.19.93-v7+ #1290 SMP Fri Jan 10 16:39:50 GMT 2020 armv7l GNU/Linux
pi@raspberrypi:~ $ cat /etc/os-release
PRETTY_NAME="Raspbian GNU/Linux 10 (buster)"
NAME="Raspbian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
VERSION_CODENAME=buster
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"
pi@raspberrypi:~ $ cat /etc/rpi-issue
Raspberry Pi reference 2019-09-26
Generated using pi-gen, https://github.com/RPi-Distro/pi-gen, 80d486687ea77d31fc3fc13cf3a2f8b464e129be, stage2
pi@raspberrypi:~ $ python3 -V
Python 3.7.3
pi@raspberrypi:~ $ sudo python3 midi/
midi_test.py   visualizer.py
pi@raspberrypi:~ $ sudo python3 midi/visualizer.py
``` 

## LED strip wiring
https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring
* Pi pin 18 to NeoPixel DIN.
* 1N4001 diode cathode (side with the stripe) to NeoPixel 5V.
* Power supply ground to Pi ground.
* Power supply ground to NeoPixel GND.
* Power supply 5V to 1N4001 diode anode (side without the stripe).
![Alt text](https://cdn-learn.adafruit.com/assets/assets/000/064/122/medium640/led_strips_raspi_NeoPixel_Diode_bb.jpg?1540315941)
