#include <Arduino.h>

#define sampleTime 100

int reading = 0;
float pot;
unsigned long lastTime = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (millis() - lastTime > sampleTime) {
    reading = analogRead(A0);
    pot = reading * (5.0 / 1023.0);
    Serial.println(pot, 3);
  }
}