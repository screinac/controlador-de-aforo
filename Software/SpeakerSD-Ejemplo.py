import os
import time
from machine import Pin, SoftSPI
from sdcard import SDCard
from wavplayer import WavPlayer

SCK_PIN = 21
WS_PIN = 22
SD_PIN = 19
I2S_ID=1
BUFFER_LENGTH_IN_BYTES=40000;

wp = WavPlayer(id=I2S_ID, 
               sck_pin=Pin(SCK_PIN), 
               ws_pin=Pin(WS_PIN), 
               sd_pin=Pin(SD_PIN), 
               ibuf=BUFFER_LENGTH_IN_BYTES)

spisd = SoftSPI(-1, miso=Pin(16), mosi=Pin(5), sck=Pin(17))
sd = SDCard(spisd, Pin(18))



print('Root directory:{}'.format(os.listdir()))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
print('Root directory:{}'.format(os.listdir()))
os.chdir('sd')
print('SD Card contains:{}'.format(os.listdir()))


#wp.play("Gaur Plains.wav", loop=False)
# wait until the entire WAV file has been played

#while wp.isplaying() == True:
#    print('Holi')
#    time.sleep(5)
    


#time.sleep(5)
#wp.pause()

wp.play("The Rare Occasions.wav", loop=False)
# # wait until the entire WAV file has been played
while wp.isplaying() == True:
    print('Holi')
    time.sleep(5)
    

# wp.play("Midwinters.wav", loop=False)
# # wait until the entire WAV file has been played
# while wp.isplaying() == True:
#     print('Holi')
#     time.sleep(5)
    

# wp.play("Take.wav", loop=False)
# # wait until the entire WAV file has been played
# while wp.isplaying() == True:
#     print('Holi')
#     time.sleep(5)
    

wp.play("Possessed by Disease.wav", loop=False)
# wait until the entire WAV file has been played
while wp.isplaying() == True:
    print('Holi')
    time.sleep(5)
    

