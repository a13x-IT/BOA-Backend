#include <NetworkingServer.h> // Include the header file

namespace Networking
{
  server::server(int port, IPAddress address, uint8_t analogPin, int ADCbits)  : ip(address), Eth_server(port), hardware(analogPin, ADCbits)
  {
    Serial.begin(115200);
    Ethernet.begin(mac, ip);
    Eth_server.begin();
    Serial.println("Server started");
    // this->analogPort = analogPin;
    // this->ADCBits = ADCbits;
    Hardwareinterface::analogIn hardware(analogPin, ADCbits);
  }
  
  server::~server()
  {
    Serial.end();
  }

  void server::sendData()
  {
    EthernetClient client = Eth_server.available();

    if (client) {
      Serial.println("New client");
      while (client.connected()) {
        if (client.available()) {
          char c = client.read();
          Serial.write(c); // Print the received character to the Serial Monitor

          // If the client sends a GET request, respond with the analog input data
          if (c == '\n') {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-Type: text/plain");
            client.println();
            client.println(hardware.getData());
            break;
          }
        }
      }
      client.stop();
      Serial.println("Client disconnected");
    }
  }
} // namespace Networking
