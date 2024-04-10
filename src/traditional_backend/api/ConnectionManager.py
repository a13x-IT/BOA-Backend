from fastapi import WebSocket
from random import randrange
from api.models import Distance
from fastapi.encoders import jsonable_encoder
from api.data_processing import data_processing
from api.utils import average

class ConnectionManager:
  """Class defining the Distance Websocket events"""
  def __init__(self) -> None:
    """init method, keeping track of connections"""
    self.active_connections = []

  async def connect(self, websocket: WebSocket):
    """connect event"""
    await websocket.accept()
    self.active_connections.append(websocket)
  
  async def send_distance(self, websocket : WebSocket):
    """Sends the Distance"""
    distance = [data_processing.receive_data(), data_processing.receive_data(), data_processing.receive_data()]
    #distance = [randrange(2,200),randrange(50,150),randrange(1,200)]
    distance = Distance(distance=distance,avg_distance=average(distance),unit="cm")
    payload = jsonable_encoder(distance)
    await websocket.send_json(payload)
  
  async def send_distance_corrected(self, websocket: WebSocket): 
    raise NotImplementedError
  
  def disconnect(self, websocket : WebSocket):
    """disconnect event"""
    self.active_connections.remove(websocket)