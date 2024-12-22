const int turbidityPin = A0; // Analog pin connected to the turbidity sensor
#define trigPin 3  // Trig pin of HC-SR04 connected to Arduino digital pin 9
#define echoPin 2 // Echo pin of HC-SR04 connected to Arduino digital pin 10

int waterHeight = 7; // Height of the aquarium tank in cm
float tankHeight = 15.0; // Total height of the tank (including water level) in cm
long duration;
int distance;
float waterPercentage;
unsigned long previousMillis = 0;
const long interval = 1000; // Interval to send data (milliseconds)

void setup() {
  Serial.begin(9600); // Start serial communication at 9600 baud rate
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    
    // Read turbidity value
    int turbidityValue = analogRead(turbidityPin);
    // Send the turbidity value over serial
    Serial.print("Turbidity Value: ");
    Serial.println(turbidityValue);

    // Clear the trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    // Send a 10 microsecond pulse to trigger
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Read the duration of the echo pulse
    duration = pulseIn(echoPin, HIGH);

    // Calculate distance in cm
    distance = duration * 0.034 / 2;

    // Calculate water percentage
    waterPercentage = ((tankHeight - distance) / tankHeight) * 100;

    // Ensure water percentage does not exceed 100%
    if (waterPercentage > 100) {
      waterPercentage = 100;
    }

    // Print water percentage
    Serial.print("Water Level (%): ");
    Serial.println(waterPercentage);
  }
}
