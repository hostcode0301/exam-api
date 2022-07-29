from pydantic import BaseConfig, BaseModel
import humps


class DBModel(BaseModel):
    """Config PascalCase serialization."""

    class Config(BaseConfig):
        allow_population_by_field_name = True
        alias_generator = humps.pascalize