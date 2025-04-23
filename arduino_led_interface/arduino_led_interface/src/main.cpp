#include <Arduino.h>

const int led = 2;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char read = Serial.read();
    Serial.println(read);
    
    if (read == '1') {
      digitalWrite(led, HIGH);
    }

    if (read == '0') {
      digitalWrite(led, LOW);
    }
  }
}