import os

from pydantic import BaseSettings

DESCRIPTION = """
## Overview

- **default**: Check health of the application

"""

class Settings(BaseSettings):
    app_name: str = "Exam APIs"
    api_prefix: str = "/api"
    description: str = DESCRIPTION
    # 10MB
    max_size_upload = 1024 * 1024 * 10
    max_workers: int = 3
    debug: bool = True
    origin = ["http://localhost:3000"]

class DevSettings(Settings):
    dynamodb_tbl = 'dev.exam'
    dynamodb_enpoint_url = 'http://localhost:8000'

class StagingSettings(Settings):
    dynamodb_tbl = 'staging.exam'
    dynamodb_enpoint_url = 'http://localhost:8000'

class ProdSettings(Settings):
    dynamodb_tbl = 'prod.exam'
    dynamodb_enpoint_url = 'http://localhost:8000'

def get_settings():
    env = os.environ.get('env', None)

    if env == 'prod':
        return ProdSettings()
    elif env == 'staging':
        return StagingSettings()
    
    return DevSettings()

config = get_settings()