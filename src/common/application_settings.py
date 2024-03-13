import os
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)
# from common.app_configuration_settings_source import AppConfigurationSettingsSource


class ApplicationSettings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__", extra="ignore")
    # @classmethod
    # def settings_customise_sources(
    #     cls,
    #     settings_cls: type[BaseSettings],
    #     init_settings: PydanticBaseSettingsSource,
    #     env_settings: PydanticBaseSettingsSource,
    #     dotenv_settings: PydanticBaseSettingsSource,
    #     file_secret_settings: PydanticBaseSettingsSource,
    # ) -> tuple[PydanticBaseSettingsSource, ...]:
    #     return (
    #         env_settings,
    #         AppConfigurationSettingsSource(
    #             settings_cls, os.environ["APP_CONFIGURATION__ENDPOINT"]
    #         ),
    #     )
    GLOBAL__ENVIRONMENT: str = "dev"
    
    OPEN_AI__API_KEY: str = "14cb2269883c4138a5ecb3e773fd3ce7"
    OPEN_AI__AZURE_ENDPOINT: str = "https://proyectoiaopenaifcdev.openai.azure.com/"
    OPEN_AI__API_VERSION: str = "2023-07-01-preview"
    # OPEN_AI_EMBEDDINGS__API_TYPE: str
    # OPEN_AI_EMBEDDINGS__API_KEY: str
    # OPEN_AI_EMBEDDINGS__AZURE_ENDPOINT: str
    # OPEN_AI_EMBEDDINGS__API_VERSION: str

    # QDRANT__ENDPOINT: str
    # QDRANT__API_KEY: str
    # QDRANT__PORT: int

    # APPLICATION_INSIGHTS__CONNECTION_STRING: str
 
    SQL_SERVER__HOST: str = "adp-ha.unir.net"
    SQL_SERVER__PORT: int = 22334
    SQL_SERVER__USERNAME: str = "prep.Col"
    SQL_SERVER__PASSWORD: str = "Inn0v4c10n#24"
    SQL_SERVER__NAME: str = "IA"
    
    # SQL_SERVER__CONNECTION_STRING: str
    # SQL_SERVER__HOST: str = "mssql-server-preparador-dev-we-001.database.windows.net"
    # SQL_SERVER__PORT: int = 1433
    # SQL_SERVER__USERNAME: str = "user4defOP7r479X"
    # SQL_SERVER__PASSWORD: str = "v3lllscr37-244saafD-wd33434DLz"
    # SQL_SERVER__NAME: str = "preparador"