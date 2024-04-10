from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.models import APIKey
from random import randrange
from Config.configFileUtils import read_config_entry, write_config_entry
from api.sensor import router as sensor_router
from api.setup import router as setup_router
from authentication.auth import router as auth
from camera.api import router as camera_router
from authentication.auth import api_key_auth, generate_new_api_key



app = FastAPI(
  title="BOA-API",
  summary="API for Interacting with the Hardware of the BOA-Frontend",
  version="0.0.1",
  contact= {
    "name" : "Capibarry Solutions GmbH",
    "email" : "office@capibarra.at",
    "url" : "https://capibarrysolutions.at/contact",
  },
    license_info={
      "name" : "GNU Affero General Public License v3.0 only",
      "identifier" : "AGPL-3.0-only	",
    },
)

#TODO: Change to actual url of Frontend
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



############## API ROOT LINK ###############
# @app.get("/")
# async def root(api_key: APIKey = Depends(api_key_auth)):
#   return "http://127.0.0.1:8000/docs"




def first_Setup(): 
  print("Setup in Progress")
  print(generate_new_api_key())

@app.on_event("startup")
def run_setup():
  if not read_config_entry("setup_done"):
    first_Setup()
    write_config_entry("setup_done", True)



app.include_router(sensor_router)
app.include_router(camera_router)
app.include_router(setup_router)
app.include_router(auth)
