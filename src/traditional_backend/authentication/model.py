from pydantic import BaseModel


class credentials(BaseModel):
  email: str
  apikey : str