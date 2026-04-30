from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    log_level: str = "INFO"
    telegram_bot_token: str = ""
    openai_api_key: str = ""
    database_url: str = "sqlite:///./expense_bot.db"
    default_currency: str = "AED"
    timezone: str = "Asia/Dubai"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()
