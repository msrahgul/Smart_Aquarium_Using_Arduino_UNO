from pyfirmata import Arduino, util
import time
port = 'COM11'
board = Arduino(port)

relay_pin_1 = 2
relay_pin_2 = 3

board.digital[relay_pin_1].mode = 1
board.digital[relay_pin_2].mode = 1


def switch_pumps():
    board.digital[relay_pin_1].write(1)  # Turn on relay 1
    time.sleep(5)  # Run the first pump for 2 seconds
    board.digital[relay_pin_1].write(0)  # Turn off relay 1
    time.sleep(5)  # Wait for a short time to ensure both pumps don't run simultaneously
    board.digital[relay_pin_2].write(1)  # Turn on relay 2
    time.sleep(5)  # Run the second pump for 2 seconds
    board.digital[relay_pin_2].write(0)  # Turn off relay 2
    time.sleep(5)  # Wait for a short time before restarting the loop

# Main loop
while True:
    switch_pumps()
