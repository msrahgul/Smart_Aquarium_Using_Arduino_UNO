#include <Servo.h>

Servo servoMotor;  // Create a servo object to control the servo motor
int servoPin = 9;  // The pin number to which the servo signal wire is connected

void setup() {
  servoMotor.attach(servoPin);  // Attach the servo object to the pin
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    int angle = Serial.parseInt();  // Read the angle value from serial input
    if (angle >= 0 && angle <= 90) {
      servoMotor.write(angle);  // Move the servo to the specified angle
    }
  }
}
