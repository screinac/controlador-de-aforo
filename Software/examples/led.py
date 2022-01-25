import time
import ws2812

# chain = WS2812(spi_bus=1, led_count=4)
# data = [
#     (255, 0, 0),    # red
#     (0, 255, 0),    # green
#     (0, 0, 255),    # blue
#     (85, 85, 85),   # white
# ]
# chain.show(data)

chain = ws2812.WS2812(spi_bus=1, led_count=2)
while True:
    data = [
        (255, 0, 0),    # red
        (0, 255, 0),    # green
    ]
    chain.show(data)

    time.sleep_ms(1000)

    data = [
        (0, 255, 0),    # green
        (255, 0, 0),    # red
    ]
    chain.show(data)

    time.sleep_ms(1000)