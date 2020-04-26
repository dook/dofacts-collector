from pydantic import BaseSettings


class Settings(BaseSettings):
    IMAGE_BUCKET: str

    DB_DRIVER: str
    DB_USER: str
    DB_PASSWORD: str
    DB_READER_HOST: str
    DB_WRITER_HOST: str
    DB_PORT: str
    DB_NAME: str

    RECAPTCHA_SECRET: str
    RECAPTCHA_THRESHOLD: float


settings = Settings()
