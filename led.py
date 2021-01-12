import RPi.GPIO as GPIO
import time

# blinking function
def blink(pin):
    # to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BOARD)

    # set up GPIO output channel, we set GPIO4 (Pin 7) to OUTPUT
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return



