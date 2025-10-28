import os

def _env(name, default=None): return os.getenv(name, default)

class BaseConfig:
    SECRET_KEY = _env("SECRET_KEY", "dev-secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = _env("DATABASE_URI")

class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = _env("DATABASE_URI")

def get_config(name: str | None):
    env = _env("FLASK_ENV", "development").lower()
    if env.startswith("prod"):
        return ProdConfig
    return DevConfig
