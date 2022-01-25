import machine, neopixel
import time

# number of pixels
n = 2 
# pin out
p = 16
# create the neopixel object
np = neopixel.NeoPixel(machine.Pin(p), n)

while True:
    np[0] = (255, 0, 0) #red
    np[1] = (0, 255, 0) #green
    np.write()
    time.sleep_ms(1000)

    np[0] = (0, 255, 0) #green
    np[1] = (255, 0, 0) #red
    np.write()
    time.sleep_ms(1000)