import machine
import hcsr04
import time

ultrasonic4 = hcsr04.HCSR04(trigger_pin=32, echo_pin=35, echo_timeout_us=1000000)
ultrasonic3 = hcsr04.HCSR04(trigger_pin=33, echo_pin=34, echo_timeout_us=1000000)
ultrasonic2 = hcsr04.HCSR04(trigger_pin=25, echo_pin=39, echo_timeout_us=1000000)
ultrasonic1 = hcsr04.HCSR04(trigger_pin=26, echo_pin=36, echo_timeout_us=1000000)


while True:
    distance4 = ultrasonic4.distance_cm()
    time.sleep_ms(300)
    distance3 = ultrasonic3.distance_cm()
    time.sleep_ms(300)
    distance2 = ultrasonic2.distance_cm()
    time.sleep_ms(300)
    distance1 = ultrasonic1.distance_cm()
    time.sleep_ms(1000)
    print('Distance4:', distance4, 'cm', '|', distance4/2.54, 'inch')
    print('Distance3:', distance3, 'cm', '|', distance3/2.54, 'inch')
    print('Distance2:', distance2, 'cm', '|', distance2/2.54, 'inch')
    print('Distance1:', distance1, 'cm', '|', distance1/2.54, 'inch')

    