#include <Arduino.h>
<<<<<<< Updated upstream
// #include <analogIn.h>

// Hardwareinterface::analogIn analogTest(A0,10);
void setup() {
  // put your setup code here, to run once:
  // Serial.begin(9600);
}

void loop() {
  // // put your main code here, to run repeatedly:
  // int analogData =  analogTest.getData();
  // Serial.println(analogData);
  // delay(1000);
}
=======
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

>>>>>>> Stashed changes
