#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("UWB project start");
}

void loop() {
  Serial.println("running...");
  delay(1000);
}