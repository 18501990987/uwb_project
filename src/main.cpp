#include <Arduino.h>

void printBootInfo();
void initUwbPlaceholder();
void printFakeUwbData();

void setup() {
  Serial.begin(115200);
  delay(1000);

  printBootInfo();
  initUwbPlaceholder();
}

void loop() {
  printFakeUwbData();
  delay(1000);
}

void printBootInfo() {
  Serial.println("================================");
  Serial.println("UWB project boot");
  Serial.println("Board: ESP32-S3");
  Serial.println("Role : test node");
  Serial.println("================================");
}

void initUwbPlaceholder() {
  Serial.println("[STEP] init SPI...");
  Serial.println("[STEP] init UWB module...");
  Serial.println("[OK]   placeholder ready");
}

void printFakeUwbData() {
  static unsigned long ts = 1000;

  Serial.print("ts_ms=");
  Serial.print(ts);
  Serial.print(", anchor_id=A");
  Serial.print(", range_m=1.23");
  Serial.print(", valid=1");
  Serial.print(", quality=80");
  Serial.println();

  ts += 1000;
}