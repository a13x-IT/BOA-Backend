#include <Arduino.h>
#include <math.h>
#include <analogIn.h>

using namespace Hardwareinterface;

  int analogIn::readAnalogData() {
    int value = analogRead(analogPin);
    return value;
  }

  int analogIn::convertToValue200() {
    long value = readAnalogData();
    return map(value, 0, this->aDCRange, 0, 200);
  }


  int analogIn::getData() {
    return convertToValue200();
  }

analogIn::analogIn(int Pin, int ADCBits)
{
  analogPin = Pin;
  aDCRange = pow(2,ADCBits) - 1;
}

analogIn::~analogIn()
{
}
