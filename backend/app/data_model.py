from pydantic import (
    BaseModel,
    Field
)
from typing import (
    Annotated,
)

class User_data(BaseModel):
    image: Annotated[str, Field(..., description="the value should be a base64 image string")]

class Response_data(BaseModel):
    class_folder: Annotated[int, Field(..., description="This variable hold the predicted folder label as integer")]
    
