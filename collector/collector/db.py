from sqlalchemy import Column, DateTime, MetaData, String, Table, create_engine
from sqlalchemy.engine.url import URL

from collector.config import settings
from collector.consts import COMMENT_LENGTH, TEXT_LENGTH

metadata = MetaData()
t_news_draft = Table(
    "news_draft",
    metadata,
    Column("id", String(32), primary_key=True),
    Column("reporter_email", String(254)),
    Column("comment", String(COMMENT_LENGTH)),
    Column("url", String(2000)),
    Column("text", String(TEXT_LENGTH)),
    Column("screenshot_url", String(1000)),
    Column("reported_at", DateTime()),
)


def get_db_url():
    return URL(
        drivername=settings.DB_DRIVER,
        username=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_WRITER_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME,
    )


engine = create_engine(get_db_url())


def get_db():
    with engine.begin() as connection:
        yield connection
