from sqlmodel import create_engine, SQLModel


def connect_db():
    connection_string = str("postgresql://kamilzafar54:0ubRWJhPZt3X@ep-twilight-unit-a5jmeq8q.us-east-2.aws.neon.tech/Todo?sslmode=require")

    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  