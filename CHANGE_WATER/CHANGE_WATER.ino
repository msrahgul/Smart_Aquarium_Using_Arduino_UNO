#include <NewPing.h>

#define TRIGGER_PIN  3
#define ECHO_PIN     2
#define MAX_DISTANCE 16
#define PUMP_PIN_1   6
#define PUMP_PIN_2   7

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

void setup() {
  Serial.begin(9600);
  pinMode(PUMP_PIN_1, OUTPUT);
  pinMode(PUMP_PIN_2, OUTPUT);
}

void loop() {
  delay(50);
  int distance = sonar.ping_cm();
  Serial.print(distance);
  Serial.println("cm");

  if (distance < 12) {
    digitalWrite(PUMP_PIN_1, HIGH);
    digitalWrite(PUMP_PIN_2, LOW);
    Serial.println("Relay 1 activated");
  } else if (distance > 5) {
    digitalWrite(PUMP_PIN_1, LOW);
    digitalWrite(PUMP_PIN_2, HIGH);
    Serial.println("Relay 2 activated");
  } else {
    digitalWrite(PUMP_PIN_1, HIGH);
    digitalWrite(PUMP_PIN_2, HIGH);
    Serial.println("Relays deactivated");
  }
  
  // Allow time for serial communication
  delay(100);
}
