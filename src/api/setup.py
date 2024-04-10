from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from Config.configFileUtils import read_config_entry, write_config_entry
from api.models import CorrectionSystem, SensorSystem, PostProcessing
from authentication.auth import api_key_auth
from fastapi.openapi.models import APIKey


router = APIRouter(prefix="/setup", tags=["setup"])
toggleStatus : bool

@router.get("/test-connection")
async def test_connection():
   """
   Tests the connection for any issues during setup

   Returns: 
    - True (boolean): If config is correctly defined in frontend
   """
   return True

@router.post("/set-correction")
def set_correction(correction_system : CorrectionSystem, api_key: APIKey = Depends(api_key_auth) ) -> CorrectionSystem:
  """
    Sets the correction system by updating the measured distance in the configuration.

    Parameters:
    - correction_system (CorrectionSystem): The correction system information, which includes the meassured distance in cm.

    Returns:
    The updated CorrectionSystem object.

    Raises:
    - HTTPException(422): If the measured distance is negative or exceeds the supported distance.
  """
  if correction_system.measured_distance_cm <= 0:
      error_msg = "Negative distance not possible"
      raise HTTPException(status_code=422, detail=[{"loc": ["set-correction"], "msg": error_msg, "type": "value_error"}])
  if correction_system.measured_distance_cm >= 200:
     error_msg = "It is not possible to measure over the supported distance"
     raise HTTPException(status_code=422, detail=[{"loc": ["set-correction"], "msg" : error_msg, "type" : "value_error"}])
  write_config_entry("correction_distance_cm", correction_system.measured_distance_cm)
  return correction_system

@router.get("/get-correction")
def get_correction(api_key: APIKey = Depends(api_key_auth)) -> CorrectionSystem:
  """
  Retrieves the correction system information, including the measured distance.

  Returns:
  The CorrectionSystem object containing the measured distance.
  """
  correction_distance =  CorrectionSystem(measured_distance_cm=read_config_entry("correction_distance_cm", 0))
  return correction_distance

@router.post("/set-sensors")
async def set_sensors(number: SensorSystem, api_key: APIKey = Depends(api_key_auth)) -> SensorSystem:
    """
    Sets the amount of Sensors in used for Distance Detection

    Parameters: 
    - number (SensorSystem): Retrieves a number of Sensors

    Returns:
    Returns the updated number of Sensors used

    Exception:
    - Raises a http 422 Error if the number of sensors falls under 0 or over 3
    """
    if number.number_of_sensors <= 0:
        error_msg = "Negative Sensors not possible"
        raise HTTPException(status_code=422, detail=[{"loc": ["number_of_sensors"], "msg": error_msg, "type": "value_error"}])

    if number.number_of_sensors > 3:
        error_msg = "Amount of Sensors exceeds shield"
        raise HTTPException(status_code=422, detail=[{"loc": ["number_of_sensors"], "msg": error_msg, "type": "value_error"}])


    write_config_entry('number_of_sensors', number.number_of_sensors)
    return number



@router.get("/get-sensors")
async def get_sensors(api_key: APIKey = Depends(api_key_auth)) -> SensorSystem:
     # Read the number of sensors from the specific entry in the config file
    number_of_sensors = SensorSystem(number_of_sensors=read_config_entry('number_of_sensors', 0))
  
    return number_of_sensors

@router.post("/set-data-processing")
async def set_data_processing(postProcessing:PostProcessing, api_key: APIKey = Depends(api_key_auth)) -> PostProcessing:
   toggleStatus = postProcessing.toggleStatus
   return toggleStatus



  
