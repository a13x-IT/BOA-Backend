#ifndef NETWORKING_SERVER_H
#define NETWORKING_SERVER_H

#include <SPI.h>
#include <Ethernet.h>
#include <analogIn.h>

namespace Networking
{
  class server
  {
  private:
    IPAddress ip;
    byte mac[6] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED }; // MAC address
    EthernetServer Eth_server;
    uint8_t analogPort = A0;
    int ADCBits = 10;
    Hardwareinterface::analogIn hardware;

  public:
    server(int port, IPAddress address, uint8_t analogPort, int ADCBits);
    ~server();
    void sendData();
  };
} // namespace Networking

#endif // NETWORKING_SERVER_H
