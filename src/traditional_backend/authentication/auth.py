from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, APIRouter
from starlette.status import HTTP_401_UNAUTHORIZED
from Config.configFileUtils import read_config_entry, write_config_entry
from authentication.model import credentials
from functools import lru_cache
import secrets

router = APIRouter(prefix="/auth", tags=["auth"])

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

@lru_cache(maxsize=None)
async def api_key_auth(api_key: str = Security(api_key_header)):
    if api_key != read_config_entry("apikey"):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Missing or invalid API key")
    else:
        return
    
def generate_new_api_key():
    key = secrets.token_urlsafe(16)
    write_config_entry("apikey", key)
    return key

def authenticate_user(email: str, apikey: str):
    email_file = read_config_entry("email")
    apikey_file = read_config_entry("apikey")

    if email == email_file and apikey == apikey_file:
        return True
    else:
        return False

# New route for login
@router.post("/login")
async def login(credentials : credentials):
    user = authenticate_user(credentials.email, credentials.apikey)
    if user:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        