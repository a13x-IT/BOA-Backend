from pydantic import BaseModel, Field

#TODO: implement error checks

class SensorSystem(BaseModel):
  number_of_sensors : int #No error checks here as the code does not work without it rn

class CorrectionSystem(BaseModel):
  measured_distance_cm : int #= Field(ge=0, le=200, default=200)


class StreamSystem(BaseModel):
  stream: bool = Field(default=False)
  audio: bool = Field(default=False)
  smoothing: bool = Field(default=False)

class Distance(BaseModel):
  distance: list[int]
  avg_distance : int
  unit : str

class PostProcessing(BaseModel):
  toggleStatus: bool