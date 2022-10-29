from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from standard.configs.app import appConfigs

if appConfigs.DB_CONNECTION == 'mysql':
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{}:{}@{}/{}".format(
        appConfigs.DB_USER,
        appConfigs.DB_PASSWORD,
        appConfigs.DB_HOST,
        appConfigs.DB_DATABASE
    )
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
elif appConfigs.DB_CONNECTION == 'postgresql':
    SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(
        appConfigs.DB_USER,
        appConfigs.DB_PASSWORD,
        appConfigs.DB_HOST,
        appConfigs.DB_DATABASE
    )
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./standard.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DBModel = declarative_base()


def init_db():
    DBModel.metadata.create_all(bind=engine)
