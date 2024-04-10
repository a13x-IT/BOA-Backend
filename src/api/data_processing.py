from smbus import SMBus
from api.const import const
class data_processing:
    

    i2c_bus = 1
    device_address = 0x33

    bus = SMBus(i2c_bus)

    # Depricated
    i = 0

    def __init__(self):
        self.previous_distances = []
    ####

    async def receive_data(self):
        """
        Gets the data from the Sensors and changes it from Volts to CM
    try:
    - recieves the data and returns it

    except:
    - if something goes wrong it throws an error

    finally:
    - closes the i2c connection
        """
        try:    
            received_data = self.bus.read_i2c_block_data(self.device_address)
            ready_data = self.convert_volt_to_cm(received_data)
            return ready_data
    
    
        except IOError as e:
            print("Something doesn't work")

        finally:
            self.bus.close()

    #### Depricated
    async def receive_processed_data(self):
        try:    
            received_data = self.bus.read_i2c_block_data(self.device_address)
            distance = self.convert_volt_to_cm(received_data) 
            self.previous_distances.append(distance)
            self.previous_distances = self.previous_distances[-10:]
            is_distance_correct = self.is_distance_correct(distance)
            if is_distance_correct == True:
                i = i + 1
                return received_data
            else:
                if i < 9:
                    i= i + 1
                    return self.previous_distances[i-2]
                elif i == 9:
                    return self.previous_distances[8]


        except IOError as e:
            print("Something doesn't work")

        finally:
            self.bus.close()
    #####
            
    async def convert_volt_to_cm(digitalValue):
        """
        Changes the volts from the i2c connection to cm
        """
       

        analog_voltage = (digitalValue / (2**const.bit_resolution - 1)) * (const.v_max - const.v_min) + const.v_min


        distance = const.d_min + (analog_voltage - const.v_min) / (const.v_max - const.v_min) * (const.d_max - const.d_min)

        return distance
        

    async def is_distance_correct(self, current_distance):
        """
        checks if the current value is near to the last values to prevent failures
        
        DEPRICATED
        """
        if len(self.previous_distances) > 0:
                average_distance = sum(self.previous_distances) / len(self.previous_distances)
                tolerance = 10 
                return abs(current_distance - average_distance) <= tolerance
        else:
            # If there are no previous distances, consider it correct
            return True

