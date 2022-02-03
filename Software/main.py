import time
import os
import network
import socket
import tm1637
import hcsr04
from machine import Pin, SoftSPI
from neopixel import NeoPixel
from sdcard import SDCard
from wavplayer import WavPlayer
from micropython import const


spisd = SoftSPI(-1, miso=Pin(16), mosi=Pin(5), sck=Pin(17))
sd = SDCard(spisd, Pin(18))

Ultra1 = hcsr04.HCSR04(trigger_pin=26, echo_pin=36, echo_timeout_us=1000000)
Ultra2 = hcsr04.HCSR04(trigger_pin=25, echo_pin=39, echo_timeout_us=1000000)
Ultra3 = hcsr04.HCSR04(trigger_pin=33, echo_pin=34, echo_timeout_us=1000000)
Ultra4 = hcsr04.HCSR04(trigger_pin=32, echo_pin=35, echo_timeout_us=1000000)

NUM_OF_LED = 1
led = NeoPixel(Pin(23), NUM_OF_LED)

SCK_PIN = 21
WS_PIN = 22
SD_PIN = 19
I2S_ID=1
BUFFER_LENGTH_IN_BYTES=32000

wp = WavPlayer(id=I2S_ID, 
               sck_pin=Pin(SCK_PIN), 
               ws_pin=Pin(WS_PIN), 
               sd_pin=Pin(SD_PIN), 
               ibuf=BUFFER_LENGTH_IN_BYTES)

p12=Pin(12,Pin.IN,Pin.PULL_DOWN)
p14=Pin(14,Pin.IN,Pin.PULL_DOWN)
p27=Pin(27,Pin.IN,Pin.PULL_DOWN)

display = tm1637.TM1637(clk=Pin(15), dio=Pin(13))



def Botonirq3(pin):
    global personas
    personas =0
    time.sleep_ms(250)

def Botonirq2(pin):
    global personas
    personas -=1
    time.sleep_ms(250)

def Botonirq1(pin):
    global personas
    personas +=1
    time.sleep_ms(250)      

p12.irq(handler=Botonirq3,trigger=Pin.IRQ_FALLING)
p14.irq(handler=Botonirq2,trigger=Pin.IRQ_FALLING)
p27.irq(handler=Botonirq1,trigger=Pin.IRQ_FALLING)

timewrite=time.ticks_ms()


wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface

def wifiConect():
    
    if not wlan.isconnected():
        for i in range(TIMEOUT):
            if wlan.status() == 1001:
                break
            else:
                wlan.connect(ssid,password)
        else:
            raise OSError("timeout waiting for response")

vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
os.chdir('sd')

TIMEOUT = const(100)
limite_mayor = 4.5 #m^2
limite_inferior = 10 #m^2
distancia_paso = 13 #cm

#Variables Ultrasonido-1
entrada1=0
salida1=0
proteccion1=0

#Variables Ultrasonido-2
entrada2=0
salida2=0
proteccion2=0

#Variables Ultrasonido-3
entrada3=0
salida3=0
proteccion3=0

#Variables Ultrasonido-4
entrada4=0
salida4=0
proteccion4=0

proteccionAudio=0


ssid = 'FAMILIA GORDILLO 2.4'
password = 'gordillo2089'

personas=5
espacio = 60
modo_ultrasonido = 4
ejecucion = True 

writechar=''

with open('config.txt',"r") as archivo:
    for linea in archivo.readlines():
        linea=linea.strip('\n')
        linea=linea.split('=')
        
        if 'ssid' in linea:
            ssid=linea[1]
        if 'password' in linea:
            password=linea[1]
        if 'limite_mayor' in linea:
            limite_mayor=float(linea[1])
        if 'limite_inferior' in linea:
            limite_inferior=float(linea[1])
        if 'distancia_paso' in linea:
            distancia_paso=float(linea[1])
        if 'espacio' in linea:
            espacio=float(linea[1])
        if 'modo_ultrasonido' in linea:
            modo_ultrasonido=int(linea[1])
        if 'personas' in linea:
            personas=int(linea[1])



relacion=personas/espacio

if (relacion > 1/limite_mayor):
    led[0] = (255, 0, 0)
    led.write()
elif (relacion > 1/limite_inferior):
    led[0] = (255, 112, 0)
    led.write()
else:
    led[0] = (63, 218, 5)
    led.write()  

display.number(personas)

wifiConect()

##Extraer datos Internet - Actualizar 

while ejecucion:
    if (modo_ultrasonido == 1): #entrada bidireccional - entrada bidireccional
            
            #Ultrasonido Bidireccional - 1
            distanciau1 = Ultra1.distance_cm()
            time.sleep_ms(50)
            distanciau2 = Ultra2.distance_cm()
            time.sleep_ms(50)
            if((distanciau1 < distancia_paso) and (distanciau2 >= distancia_paso)):
                if(proteccion1==0):
                    if(salida1==1):
                        personas -=1
                        salida1=0
                        proteccion1=1
                    else:
                        entrada1=1
            elif((distanciau1 >= distancia_paso) and (distanciau2 < distancia_paso)):
                if(proteccion1==0):
                    if(entrada1==1):
                        personas +=1
                        entrada1=0
                        proteccion1=1

                    else:
                        salida1=1

            if((distanciau1 >= distancia_paso) and (distanciau2 >= distancia_paso)):
                proteccion1=0
      

            #Ultrasonido Bidireccional - 2
            distanciau3 = Ultra3.distance_cm()
            time.sleep_ms(50)
            distanciau4 = Ultra4.distance_cm()
            time.sleep_ms(50)
            if((distanciau3 < distancia_paso) and (distanciau4 >= distancia_paso)):
                if(proteccion2==0):
                    if(salida2==1):
                        personas -=1
                        salida2=0
                        proteccion2=1
                    else:
                        entrada2=1
            elif((distanciau3 >= distancia_paso) and (distanciau4 < distancia_paso)):
                if(proteccion2==0):
                    if(entrada2==1):
                        personas +=1
                        entrada2=0
                        proteccion2=1

                    else:
                        salida2=1

            if((distanciau3 >= distancia_paso) and (distanciau4 >= distancia_paso)):
                proteccion2=0

    elif (modo_ultrasonido == 2): #entrada bidireccional - entrada - entrada
            
        #Ultrasonido Bidireccional - 1
        distanciau1 = Ultra1.distance_cm()
        time.sleep_ms(50)
        distanciau2 = Ultra2.distance_cm()
        time.sleep_ms(50)
        if((distanciau1 < distancia_paso) and (distanciau2 >= distancia_paso)):
            if(proteccion1==0):
                if(salida1==1):
                    personas -=1
                    salida1=0
                    proteccion1=1
                else:
                    entrada1=1
        elif((distanciau1 >= distancia_paso) and (distanciau2 < distancia_paso)):
            if(proteccion1==0):
                if(entrada1==1):
                    personas +=1
                    entrada1=0
                    proteccion1=1

                else:
                    salida1=1

        if((distanciau1 >= distancia_paso) and (distanciau2 >= distancia_paso)):
            proteccion1=0
      

        #Ultrasonido Entrada - 1
        distanciau3 = Ultra3.distance_cm()
        time.sleep_ms(50)
        if((distanciau3 < distancia_paso)):
            if(proteccion2==0):
                personas +=1
                proteccion2=1
                
        if((distanciau3 >= distancia_paso)):
            proteccion2=0


        #Ultrasonido Entrada - 2
        distanciau4 = Ultra4.distance_cm()
        time.sleep_ms(50)
        if((distanciau4 < distancia_paso)):
            if(proteccion3==0):
                
                personas +=1
                proteccion3=1
            
        if((distanciau4 >= distancia_paso)):
            proteccion3=0



    elif (modo_ultrasonido == 3): #entrada bidireccional - entrada - salida
            
        #Ultrasonido Bidireccional - 1
        distanciau1 = Ultra1.distance_cm()
        time.sleep_ms(50)
        distanciau2 = Ultra2.distance_cm()
        time.sleep_ms(50)
        if((distanciau1 < distancia_paso) and (distanciau2 >= distancia_paso)):
            if(proteccion1==0):
                if(salida1==1):
                    personas -=1
                    salida1=0
                    proteccion1=1
                else:
                    entrada1=1
        elif((distanciau1 >= distancia_paso) and (distanciau2 < distancia_paso)):
            if(proteccion1==0):
                if(entrada1==1):
                    personas +=1
                    entrada1=0
                    proteccion1=1

                else:
                    salida1=1

        if((distanciau1 >= distancia_paso) and (distanciau2 >= distancia_paso)):
            proteccion1=0
      

        #Ultrasonido Entrada - 1
        distanciau3 = Ultra3.distance_cm()
        time.sleep_ms(50)
        if((distanciau3 < distancia_paso)):
            if(proteccion2==0):
                personas +=1
                proteccion2=1
                
        if((distanciau3 >= distancia_paso)):
            proteccion2=0


        #Ultrasonido salida - 1
        distanciau4 = Ultra4.distance_cm()
        time.sleep_ms(50)
        if((distanciau4 < distancia_paso)):
            if(proteccion3==0):    
                personas -=1
                proteccion3=1
                
        if((distanciau4 >= distancia_paso)):
            proteccion3=0



    elif (modo_ultrasonido == 4): #entrada - entrada - entrada - entrada
            
        #Ultrasonido Entrada - 1
        distanciau1 = Ultra1.distance_cm()
        time.sleep_ms(50)
        if((distanciau1 < distancia_paso)):
            if(proteccion1==0):
                personas +=1
                proteccion1=1
                
        if((distanciau1 >= distancia_paso)):
            proteccion1=0

        #Ultrasonido Entrada - 2
        distanciau2 = Ultra2.distance_cm()
        time.sleep_ms(50)
        if((distanciau2 < distancia_paso)):
            if(proteccion2==0):
                personas +=1
                proteccion2=1
            
        if((distanciau2 >= distancia_paso)):
            proteccion2=0    
      

        #Ultrasonido Entrada - 3
        distanciau3 = Ultra3.distance_cm()
        time.sleep_ms(50)
        if((distanciau3 < distancia_paso)):
            if(proteccion3==0):
                personas +=1
                proteccion3=1
                
        if((distanciau3 >= distancia_paso)):
            proteccion3=0


        #Ultrasonido Entrada - 4
        distanciau4 = Ultra4.distance_cm()
        time.sleep_ms(50)
        if((distanciau4 < distancia_paso)):
            if(proteccion4==0):
                personas +=1
                proteccion4=1
            
        if((distanciau4 >= distancia_paso)):
            proteccion4=0

    elif (modo_ultrasonido == 5): #entrada - entrada - entrada - salida
           #Ultrasonido Entrada - 1
        distanciau1 = Ultra1.distance_cm()
        time.sleep_ms(50)
        if((distanciau1 < distancia_paso)):
            if(proteccion1==0):
                personas +=1
                proteccion1=1
                
        if((distanciau1 >= distancia_paso)):
            proteccion1=0

        #Ultrasonido Entrada - 2
        distanciau2 = Ultra2.distance_cm()
        time.sleep_ms(50)
        if((distanciau2 < distancia_paso)):
            if(proteccion2==0):
                personas +=1
                proteccion2=1
            
        if((distanciau2 >= distancia_paso)):
            proteccion2=0    
      

        #Ultrasonido Entrada - 3
        distanciau3 = Ultra3.distance_cm()
        time.sleep_ms(50)
        if((distanciau3 < distancia_paso)):
            if(proteccion3==0):
                personas +=1
                proteccion3=1
                
        if((distanciau3 >= distancia_paso)):
            proteccion3=0


        #Ultrasonido Salida - 1
        distanciau4 = Ultra4.distance_cm()
        time.sleep_ms(50)
        if((distanciau4 < distancia_paso)):
            if(proteccion4==0):
                personas -=1
                proteccion4=1
            
        if((distanciau4 >= distancia_paso)):
            proteccion4=0

    elif (modo_ultrasonido == 6): #entrada - entrada - salida - salida
            
           #Ultrasonido Entrada - 1
        distanciau1 = Ultra1.distance_cm()
        time.sleep_ms(50)
        if((distanciau1 < distancia_paso)):
            if(proteccion1==0):
                personas +=1
                proteccion1=1
                
        if((distanciau1 >= distancia_paso)):
            proteccion1=0

        #Ultrasonido Entrada - 2
        distanciau2 = Ultra2.distance_cm()
        time.sleep_ms(50)
        if((distanciau2 < distancia_paso)):
            if(proteccion2==0):
                personas +=1
                proteccion2=1
            
        if((distanciau2 >= distancia_paso)):
            proteccion2=0    
      

        #Ultrasonido Salida - 1
        distanciau3 = Ultra3.distance_cm()
        time.sleep_ms(50)
        if((distanciau3 < distancia_paso)):
            if(proteccion3==0):
                personas -=1
                proteccion3=1
                
        if((distanciau3 >= distancia_paso)):
            proteccion3=0


        #Ultrasonido Salida - 2
        distanciau4 = Ultra4.distance_cm()
        time.sleep_ms(50)
        if((distanciau4 < distancia_paso)):
            if(proteccion4==0):
                personas -=1
                proteccion4=1
            
        if((distanciau4 >= distancia_paso)):
            proteccion4=0

    elif (modo_ultrasonido == 7): #entrada - salida - salida - salida
            
           #Ultrasonido Entrada - 1
        distanciau1 = Ultra1.distance_cm()
        time.sleep_ms(50)
        if((distanciau1 < distancia_paso)):
            if(proteccion1==0):
                personas +=1
                proteccion1=1
                
        if((distanciau1 >= distancia_paso)):
            proteccion1=0

        #Ultrasonido Salida - 1
        distanciau2 = Ultra2.distance_cm()
        time.sleep_ms(50)
        if((distanciau2 < distancia_paso)):
            if(proteccion2==0):
                personas -=1
                proteccion2=1
            
        if((distanciau2 >= distancia_paso)):
            proteccion2=0    
      

        #Ultrasonido Salida - 2
        distanciau3 = Ultra3.distance_cm()
        time.sleep_ms(50)
        if((distanciau3 < distancia_paso)):
            if(proteccion3==0):
                personas -=1
                proteccion3=1
                
        if((distanciau3 >= distancia_paso)):
            proteccion3=0


        #Ultrasonido Salida - 3
        distanciau4 = Ultra4.distance_cm()
        time.sleep_ms(50)
        if((distanciau4 < distancia_paso)):
            if(proteccion4==0):
                personas -=1
                proteccion4=1
            
        if((distanciau4 >= distancia_paso)):
            proteccion4=0

    elif (modo_ultrasonido == 8): #salida - salida - salida - salida
            
            
           #Ultrasonido Salida - 1
        distanciau1 = Ultra1.distance_cm()
        time.sleep_ms(50)
        if((distanciau1 < distancia_paso)):
            if(proteccion1==0):
                personas -=1
                proteccion1=1
                
        if((distanciau1 >= distancia_paso)):
            proteccion1=0

        #Ultrasonido Salida - 2
        distanciau2 = Ultra2.distance_cm()
        time.sleep_ms(50)
        if((distanciau2 < distancia_paso)):
            if(proteccion2==0):
                personas -=1
                proteccion2=1
            
        if((distanciau2 >= distancia_paso)):
            proteccion2=0    
      

        #Ultrasonido Salida - 3
        distanciau3 = Ultra3.distance_cm()
        time.sleep_ms(50)
        if((distanciau3 < distancia_paso)):
            if(proteccion3==0):
                personas -=1
                proteccion3=1
                
        if((distanciau3 >= distancia_paso)):
            proteccion3=0


        #Ultrasonido Salida - 4
        distanciau4 = Ultra4.distance_cm()
        time.sleep_ms(50)
        if((distanciau4 < distancia_paso)):
            if(proteccion4==0):
                personas -=1
                proteccion4=1
            
        if((distanciau4 >= distancia_paso)):
            proteccion4=0
    else:
        modo_ultrasonido=1

    if(personas<0):
        personas=0

    if((time.ticks_diff(time.ticks_ms(),timewrite)>10000) and (wp.isplaying==False)):
        timewrite=time.ticks_ms()
        with open('config.txt',"w") as archivo:
            archivo.write('config\n'+'ssid='+ssid+'\n'+'password='+password+'\n'+'limite_mayor='+str(limite_mayor)+'\n'+'limite_inferior='+str(limite_inferior)+'\n'+'distancia_paso='+str(distancia_paso)+'\n'+'espacio='+str(espacio)+'\n'+'modo_ultrasonido='+str(modo_ultrasonido)+'\n'+'personas='+str(personas)+'\n')



    relacion=personas/espacio

    if (relacion > 1/limite_mayor):
        led[0] = (255, 0, 0)
        led.write()
    elif (relacion > 1/limite_inferior):
        led[0] = (255, 112, 0)
        led.write()
    else:
        led[0] = (63, 218, 5)
        led.write()  

    display.number(personas)

    if((relacion < 1/limite_mayor*1.05) and (relacion > 1/limite_mayor*0.95)):
        if (proteccionAudio==0):
            wp.play("Midwinters - 16b.wav", loop=False)
            proteccionAudio=1
    elif ((relacion < 1/limite_inferior*1.05) and (relacion > 1/limite_inferior*0.95)):
        if (proteccionAudio==0):
            wp.play("Gaur Plains - 16b.wav", loop=False)
            proteccionAudio=1

    if((relacion < 1/limite_inferior*0.8) or ((relacion > 1/limite_inferior*1.2) and (relacion < 1/limite_mayor*0.8)) or (relacion > 1/limite_mayor*1.2)):
        proteccionAudio=0






