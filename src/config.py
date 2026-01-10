from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from urllib.parse import quote_plus

class PostgreSQLConfig(BaseSettings):
    host: str = 'localhost'
    name: str
    port: int = 5432
    user: str
    password: str = ""

    model_config = SettingsConfigDict (
        env_prefix="PG_",
        env_file=Path(__file__).parent.parent / ".env",
        case_sensitive=False
    )
    
    @property
    def connection_string(self):
        return f"postgresql+asyncpg://{self.user}:{quote_plus(self.password)}@{self.host}:{self.port}/{self.name}"
