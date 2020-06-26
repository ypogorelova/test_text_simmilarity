from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Schema, BaseConfig


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime] = Schema(..., alias="createdAt")


class DBModelMixin(DateTimeModelMixin):
    id: Optional[int] = None


class RWModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_alias = True
        json_encoders = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc)
            .isoformat()
            .replace("+00:00", "Z")
        }
