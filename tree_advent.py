from gpiozero import LEDBoard,LED
from gpiozero.tools import random_values
from signal import pause
import random
import datetime
from time import sleep

dayOfM = datetime.datetime.today().day

while True:
        if dayOfM <=24:
                for x in random.sample(range(2,28),dayOfM):
                        #print(x)
                        led=LED(x)
                        led.on()
                        sleep(2)
                        led.off()
        else:
                tree = LEDBoard(*range(2,28),pwm=True)

                for led in tree:
                        led.source_delay = 0.1
                        led.source = random_values()
                pause()
        sleep(5)
