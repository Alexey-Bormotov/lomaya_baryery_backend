from pydantic import Field

from src.api.request_models.request_base import RequestBase


class TaskCreateUpdateRequest(RequestBase):
    description: str = Field(..., min_length=3, max_length=150)
    url: str = Field(..., min_length=3, max_length=150)
