from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # SERVER
    debug: bool
    host: str
    port: int

    # JWT
    secret_key: str
    algorithm: str
    access_expire_minutes: int
    refresh_expire_days: int

    # DATABASE
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    class Config:
        env_file = ".env"


settings = Settings()
