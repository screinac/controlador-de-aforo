import time
import machine

import hcsr04
import neopixel
import tm1637

# ------------ Ultrasonics instantiation ------------------
ultrasonic_L1 = hcsr04.HCSR04(trigger_pin=16, echo_pin=17, echo_timeout_us=1000000)
ultrasonic_L2 = hcsr04.HCSR04(trigger_pin=16, echo_pin=17, echo_timeout_us=1000000)
ultrasonic_R1 = hcsr04.HCSR04(trigger_pin=16, echo_pin=17, echo_timeout_us=1000000)
ultrasonic_R2 = hcsr04.HCSR04(trigger_pin=16, echo_pin=17, echo_timeout_us=1000000)

ultrasonic_L1_start = time.ticks_ms()
ultrasonic_L2_start = time.ticks_ms()
ultrasonic_R1_start = time.ticks_ms()
ultrasonic_R2_start = time.ticks_ms()

ultrasonic_L1_interval = 300
ultrasonic_L2_interval = 500
ultrasonic_R1_interval = 700
ultrasonic_R2_interval = 200



# ------------ Led RGB WS2812B instantiation --------------------

# number of pixels
n = 2 
# pin out
p = 16
# create the neopixel object
np = neopixel.NeoPixel(machine.Pin(p), n)



# ------------ Buttons instantiation ---------------
plus_btn = machine.Pin(33, machine.Pin.IN)
minus_btn = machine.Pin(32, machine.Pin.IN)
reset_btn = machine.Pin(35, machine.Pin.IN)

reset = 0



# ------------ 7 Seg tm1637 instantiation ---------------
tm = tm1637.TM1637(clk=machine.Pin(5), dio=machine.Pin(4))


# ------------- Main code -------------------------

while True:

    # Ultrasonic use
    if time.ticks_ms() - ultrasonic_L1_start >= ultrasonic_L1_interval:
            distance = ultrasonic_L1.distance_cm()
            ultrasonic_L1_start = time.ticks_ms()
    if time.ticks_ms() - ultrasonic_L2_start >= ultrasonic_L2_interval:
            distance = ultrasonic_L2.distance_cm()
            ultrasonic_L2_start = time.ticks_ms()
    if time.ticks_ms() - ultrasonic_R1_start >= ultrasonic_R1_interval:
            distance = ultrasonic_R1.distance_cm()
            ultrasonic_R1_start = time.ticks_ms()
    if time.ticks_ms() - ultrasonic_R2_start >= ultrasonic_R2_interval:
            distance = ultrasonic_R2.distance_cm()
            ultrasonic_R2_start = time.ticks_ms()



    # Led RGB use
    np[0] = (255, 0, 0) #red
    np[1] = (0, 255, 0) #green
    np.write()
    time.sleep_ms(1000)

    np[0] = (0, 255, 0) #green
    np[1] = (255, 0, 0) #red
    np.write()
    time.sleep_ms(1000)

    # Buttons use
    if plus_btn.value()==0:
        print("sumar")

    # 7 seg use
    # display "0123"
    tm.show('1234')
    tm.number(1234)

