# Import necessary libraries
from flask import Flask, render_template, request  # Import Flask for web framework
import RPi.GPIO as GPIO  # Import RPi.GPIO for GPIO control

# Create a Flask web application
app = Flask(__name__)

# Set the GPIO mode and pin number
GPIO.setmode(GPIO.BCM)  # Set the GPIO pin numbering mode to BCM
forward = 17  # Define the GPIO pin number to which the LED is connected
backward= 27
left=23
right=24
GPIO.setup(led_pin, GPIO.OUT)  # Set the LED pin as an output pin

# Define routes
@app.route("/templates")
def index():
    return render_template("index.html")  # Render the HTML template for the main page

@app.route("/turn_on")
def turn_on():
    GPIO.output(forward, GPIO.HIGH)  # Turn on the LED by setting the pin to HIGH
    return "moving forward"  # Return a message indicating that the LED is turned on

@app.route("/left")
def left():
    GPIO.output(left, GPIO.HIGH)  # Turn on the LED by setting the pin to HIGH
    return "left"  # Return a message indicating that the LED is turned on

@app.route("/back")
def back():
    GPIO.output(backward, GPIO.HIGH)  # Turn on the LED by setting the pin to HIGH
    return "back"  # Return a message indicating that the LED is turned on

@app.route("/right")
def right():
    GPIO.output(right, GPIO.HIGH)  # Turn on the LED by setting the pin to HIGH
    return "right"  # Return a message indicating that the LED is turned on


@app.route("/turn_off")
def turn_off():
    GPIO.output(forward, GPIO.LOW)  # Turn off the LED by setting the pin to LOW
    GPIO.output(backward, GPIO.LOW)
    GPIO.output(left, GPIO.LOW)
    GPIO.output(right, GPIO.LOW)
    return "LED turned off"  # Return a message indicating that the LED is turned off

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')  # Run the Flask app with debugging enabled on all available network interfaces
