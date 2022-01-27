from machine import Pin
import time
p12=Pin(12,Pin.IN,Pin.PULL_DOWN)
p14=Pin(14,Pin.IN,Pin.PULL_DOWN)
p27=Pin(27,Pin.IN,Pin.PULL_DOWN)

def Botonirq3(pin):
    print('se presiono boton3')
    time.sleep_ms(100)

def Botonirq2(pin):
    print('se presiono boton2')
    time.sleep_ms(100)

def Botonirq1(pin):
    print('se presiono boton1')  
    time.sleep_ms(100)      

p12.irq(handler=Botonirq3,trigger=Pin.IRQ_FALLING)
p14.irq(handler=Botonirq2,trigger=Pin.IRQ_FALLING)
p27.irq(handler=Botonirq1,trigger=Pin.IRQ_FALLING)


while True:
    print('Holi')
    time.sleep_ms(100)

