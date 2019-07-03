from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData
from sqlalchemy.orm import load_only, joinedload

def get_session(connection_string):
    engine = create_engine(connection_string)    
    DBSession = sessionmaker(bind=engine)
    return DBSession(), engine

def get_db_object(table_name, session):
    meta = MetaData()
    meta.reflect(bind=session.get_bind())
    return meta.tables[table_name]

def get_table_session(session, table):
    return session.query(table).session

session, engine = get_session("postgres://postgres_user:1234@localhost/test_db")
person_table = get_db_object("person", session)
#result = session.query(person_table).session.execute("SELECT * FROM person;").connection.execute("SELECT name FROM person;").fetchall()
#result = session.query(person_table).count()
query = "SELECT * FROM person;"
#result = session.query(query).connection.execute(
#    "SELECT name FROM person;"
#).fetchall()
#table_session = get_table_session(session, person_table)
#result = table_session.execute("SELECT * FROM person;").fetchall()
import code
code.interact(local=locals())
