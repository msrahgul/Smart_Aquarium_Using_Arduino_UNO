import serial
import time

# Configure the serial port
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to match your Arduino's serial port

# Define relay commands
RELAY_1_ON = b'1'
RELAY_1_OFF = b'2'
RELAY_2_ON = b'3'
RELAY_2_OFF = b'4'


# Function to send relay commands
def control_relays(command):
    ser.write(command)


# Main program loop
try:
    # Wait for Arduino to signal readiness
    while True:
        if ser.readline().strip() == b'Ready':
            print("Arduino is ready")
            break

    while True:
        distance_str = ser.readline().decode().strip()
        if distance_str:
            distance = int(distance_str[:-2])
            print("Distance:", distance, "cm")

            if distance < 12:
                control_relays(RELAY_1_ON)
            elif distance > 5:
                control_relays(RELAY_2_ON)
            else:
                control_relays(RELAY_1_OFF)
                control_relays(RELAY_2_OFF)

        time.sleep(1)

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed")
