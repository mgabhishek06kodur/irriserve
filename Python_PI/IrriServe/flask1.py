from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # Sets up the RPi lib to use the Broadcom pin mappings
                        #  for the pin names. This corresponds to the pin names
                        #  given in most documentation of the Pi header
GPIO.setwarnings(False) # Turn off warnings that may crop up if you have the
                        #  GPIO pins exported for use via command line
GPIO.setup(2, GPIO.OUT) # Set GPIO2 as an output

app = Flask(__name__)  
@app.route('/')
def index():
      return 'Hello world'

if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0')
