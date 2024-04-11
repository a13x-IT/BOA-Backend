#include <Arduino.h>
#include <ArduinoJson.h>
#include <ArduinoHttpClient.h>
#include <Ethernet.h>

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress server(192, 168, 1, 100);

void setup() {
  Serial.begin(9600);
  Ethernet.begin(mac);
}

void loop() {
  // put your main code here, to run repeatedly:
}

