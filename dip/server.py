from flask import Flask
from flask import request
import RPi.GPIO as GPIO
from time import sleep
#sudo netstat -tulnp | grep :5000
#sudo kill xxxx 

LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/')
def index():
    return 'Hello flask!'
@app.route('/cakes')
def cakes():
    global val
    return "Yummy cakes!" + val
@app.route('/hello/<name>')
def hello(name):
    global val
    val = name
    return name

@app.route('/LED/ON')
def ON():
    GPIO.output(LED, 1)
    return "LED ON!"

@app.route('/LED/OFF')
def OFF():
    GPIO.output(LED, 0)
    return "LED OFF!"

@app.route('/auto')

def auto():
    global val
    val = "auto"
    while(val == "auto"):
        GPIO.output(LED, 0)
        sleep(1)
        GPIO.output(LED, 1)
        sleep(1)
    return "Auto mode!"

@app.route('/stop')
def stop():
    global val
    val = "stop"
    return "LED OFF!"


@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'   


if __name__ == '__main__':
    print('Func_called - main')
    app.run(debug = True, host = '0.0.0.0',port=5000)
    GPIO.cleanup()   
else:
    print('Func_called - imported')
