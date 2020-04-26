from sqlalchemy import create_engine

from collector.db import get_db_url, metadata

engine = create_engine(get_db_url())

metadata.create_all(engine, checkfirst=True)
