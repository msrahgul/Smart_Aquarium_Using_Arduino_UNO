import pyfirmata
import time

# Define the port where your Arduino is connected
PORT = 'COM11'  # Change this to the port where your Arduino is connected

# Initialize the Arduino board
board = pyfirmata.Arduino(PORT)

# Define the pin for the built-in LED (pin 13)
led_pin = board.get_pin('d:13:o')  # Set pin 13 as output

# Main loop to blink the LED
try:
    while True:
        # Turn the LED on (set pin HIGH)
        led_pin.write(1)
        print("LED ON")
        time.sleep(1)  # Wait for 1 second

        # Turn the LED off (set pin LOW)
        led_pin.write(0)
        print("LED OFF")
        time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    # Close the serial connection and exit gracefully on KeyboardInterrupt
    board.exit()
