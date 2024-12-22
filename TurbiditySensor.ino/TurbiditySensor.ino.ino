const int turbidityPin = A0; // Analog pin connected to the turbidity sensor
int turbidityValue = 0; // Variable to store turbidity value

void setup() {
  Serial.begin(9600); // Start serial communication at 9600 baud rate
}

void loop() {
  // Read turbidity value
  turbidityValue = analogRead(turbidityPin);
  
  // Send the turbidity value over serial
  Serial.println(turbidityValue);
  
  delay(1000); // Adjust delay as needed
}
