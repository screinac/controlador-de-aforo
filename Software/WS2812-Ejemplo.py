# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com

from machine import Pin
from neopixel import NeoPixel

NUM_OF_LED = 1
np = NeoPixel(Pin(23), NUM_OF_LED)


# # The following lines of codes should be tested using the REPL
# # Syntax:
# #    np[] = (, , )
# #    np.write()
# # ------------------------------------------------------------
# # 1. To set the 1st neopixel to red color:
np[0] = (91, 9, 9)
np.write()
# 
# # 2. To set the 4th neopixel to green color:
# np[3] = (0, 255, 0)
# np.write()
# 
# # 3. To set the 5th and 7th neopixel to blue color:
# np[4] = (0, 0, 255)
# np[6] = (0, 0, 255)
# np.write()
# 
# # 4. To set the 1st to red color,
# #               3rd to green color, and
# #               5th to blue color
# np[0] = (255, 0, 0)
# np[2] = (0, 255, 0)
# np[4] = (0, 0, 255)
# np.write()
# 
# # 5. The value given to each neopixel LED
# #    represents its brightness
# np[0] = (1, 0, 0)
# np.write()
# 
# # 6. To turn OFF all neopixel:
# for npixel in range(16):
#     np[npixel] = (0, 0, 0)
#     np.write()