from bottle import route, run
import RPi.GPIO as GPIOGPIO.setmode(GPIO.BCM)

led_pins = [13,14]
led_states = [0,0]
btn_pin = 21
GPIO.setup(led_pins[0], GPIO.OUT) GPIO.setup(led_pins[1],GPIO.OUT)
GPIO.setup(btn_pin,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
def btn_status():
    state = GPIO.input(btn_pin)
    if(state):
        return 'Up'
    else:
        return 'Down'

def html_for_led(led):
    l = str(led)
    result = "<input type = 'button' onClick = 'changed(" + l +")' value = 'LED " + l + "'/>"
