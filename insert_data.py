from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generate_database import Address, Base, Person

def generate_session():
    engine = create_engine("postgres://postgres_user:1234@localhost/test_db")

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)

    return DBSession()

if __name__ == '__main__':
    session = generate_session()
    new_person = Person(name='new person')
    session.add(new_person)
    session.commit()

    new_address = Address(post_code='00000', person=new_person)
    session.add(new_address)
    session.commit()

