#ifndef ANALOGIN_H
#define ANALOGIN_H

#include <Arduino.h>

namespace Hardwareinterface {
  
  class analogIn {
    private:
      int analogPin;
      int aDCRange;

      int readAnalogData();
      int convertToValue200();
      
    public:
      // Constructor
      analogIn(int Pin, int ADCBits);
      
      // Destructor
      ~analogIn();

      // Method to read analog data
      int getData();
  };
  
} // End of namespace HardwareInterface

#endif // ANALOGIN_H
