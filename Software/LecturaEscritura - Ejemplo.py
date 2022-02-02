import os
from machine import Pin, SoftSPI
from sdcard import SDCard

spisd = SoftSPI(-1, miso=Pin(16), mosi=Pin(5), sck=Pin(17))
sd = SDCard(spisd, Pin(18))



print('Root directory:{}'.format(os.listdir()))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
print('Root directory:{}'.format(os.listdir()))
os.chdir('sd')
print('SD Card contains:{}'.format(os.listdir()))

# with open('config.txt',"r") as archivo:
#     for linea in archivo.readlines():
#         linea=linea.strip('\n')
#         linea=linea.split('=')
        
#         if 'ssid' in linea:
#             ssid=linea[1]
#         if 'password' in linea:
#             password=linea[1]
#         if 'limite_mayor' in linea:
#             limite_mayor=float(linea[1])
#         if 'limite_inferior' in linea:
#             limite_inferior=float(linea[1])
#         if 'distancia_paso' in linea:
#             distancia_paso=float(linea[1])
#         if 'espacio' in linea:
#             espacio=float(linea[1])
#         if 'modo_ultrasonido' in linea:
#             modo_ultrasonido=int(linea[1])
#         if 'personas' in linea:
#             personas=int(linea[1])


# print(ssid)
# print(password)
# print(limite_mayor)
# print(limite_inferior)
# print(distancia_paso)
# print(espacio)
# print(modo_ultrasonido)
# print(personas)
ssid='FAMILIA GORDILLO 2.4'
password='gordillo2089'
limite_mayor = 4.5
limite_inferior = 10
distancia_paso = 13
espacio = 200
modo_ultrasonido = 1
personas = 10

# writechar='config\n'+'ssid='+ssid+'\n'+'password='+password+'\n'+'limite_mayor='+str(limite_mayor)+'\n'+'limite_inferior='+str(limite_inferior)+'\n'+'distancia_paso='+str(distancia_paso)+'\n'+'espacio='+str(espacio)+'\n'+'modo_ultrasonido='+str(modo_ultrasonido)+'\n'+'personas='+str(personas)+'\n'

# with open('config.txt',"w") as archivo:
#     archivo.write(writechar)


print('informacion en TXT')
with open('config.txt',"r") as archivo:
    print(archivo.read())
