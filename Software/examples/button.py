import machine
import time

red = machine.Pin(27, machine.Pin.OUT)
grn = machine.Pin(26, machine.Pin.OUT)
blu = machine.Pin(25, machine.Pin.OUT)

mode = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)
left = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)
rght = machine.Pin(35, machine.Pin.IN)
entr = machine.Pin(34, machine.Pin.IN)