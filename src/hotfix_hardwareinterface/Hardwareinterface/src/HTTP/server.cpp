#include <NetworkingServer.h> // Include the header file

namespace Networking
{
  server::server(int port, IPAddress address, uint8_t analogPin, int ADCbits)  : ip(address), Eth_server(port), hardware(analogPin, ADCbits)
  {
    Serial.begin(115200);
    Ethernet.begin(mac, ip);
    Eth_server.begin();
    Serial.println("Server started");
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
    String request = "";
    
    // Read the HTTP request
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        request += c;
        
        // Check for end of HTTP request
        if (request.endsWith("\r\n\r\n")) {
          break;
        }
      }
    }
    
    // Respond to the HTTP request
    if (request.startsWith("GET")) {
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: text/plain");
      client.println();
      client.println(hardware.getData());
    } else {
      client.println("HTTP/1.1 400 Bad Request");
    }

    client.stop();
    Serial.println("Client disconnected");
  }
  }

} // namespace Networking
