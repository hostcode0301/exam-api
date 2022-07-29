import datetime
from pydantic import BaseConfig, BaseModel


def convert_datetime_to_realworld(dt: datetime.datetime) -> str:
    """Convert from datetime to iso format"""

    return dt.replace(tzinfo=datetime.timezone.utc).isoformat(' ')


def convert_field_to_camel_case(string: str) -> str:
    """Convert from snake_case to camelCase"""

    return "".join(
        word if index == 0 else word.capitalize()
        for index, word in enumerate(string.split("_"))
    )

class RWModel(BaseModel):
    """Config JSON serialization to camelCase & DateTime format."""

    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {datetime.datetime: convert_datetime_to_realworld}
        alias_generator = convert_field_to_camel_case
