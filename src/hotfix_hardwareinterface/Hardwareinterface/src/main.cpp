#include <Arduino.h>
#include <ArduinoJson.h>
#include <ArduinoHttpClient.h>
#include <Ethernet.h>
#include <networkingServer.h>

int port = 8050;
IPAddress ip = (192,168,13,240);
Networking::server httpServer(port,ip,A0,10);

void setup() {
}

void loop() {
  httpServer.sendData();
}

