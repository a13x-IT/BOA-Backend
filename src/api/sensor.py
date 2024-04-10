import asyncio
import json
import random
from fastapi import APIRouter, WebSocket, HTTPException, Depends, WebSocketDisconnect
from Config.configFileUtils import read_config_entry, write_config_entry
from api.models import Distance
from fastapi.openapi.models import APIKey
from api.ConnectionManager import ConnectionManager
from api.utils import average


from authentication.auth import api_key_auth

router = APIRouter(prefix="/sensor", tags=["sensor"])

delay_between_measurements : float = 1.

manager = ConnectionManager()



@router.get("/get-distance-single")
async def get_distance_single(api_key : APIKey = Depends(api_key_auth)) -> Distance:
    lst = [100,0,0]
    distance = Distance(distance=lst,avg_distance=average(lst), unit="cm")
    return distance


@router.websocket("/get-distance")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True: 
            await asyncio.sleep(delay_between_measurements)
            await manager.send_distance(websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
