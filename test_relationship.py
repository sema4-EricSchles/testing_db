from generate_database import Person, Address
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from generate_database import Address, Base, Person
import code

engine = create_engine("postgres://postgres_user:1234@localhost/test_db")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

def method_one(session):
    has_children = Person.children.any()
    q = session.query(Person, has_children)
    for parent, has_children in q.all():
        print(parent.name, has_children)

def method_two(session):
    subq = (
        session.query(Address.person_id, func.count(Address.id).label("num_children"))
        .group_by(Address.person_id)
        .subquery()
    )
    q = (session
         .query(Person, subq.c.num_children)
         .outerjoin(subq, Person.id == subq.c.person_id)
         )
    for parent, has_children in q.all():
        print(parent.name, has_children)

def method_three(session):
    q = (session
         .query(Person, func.count(Address.id).label("num_children"))
         .outerjoin(Address, Person.children)
         .group_by(Person)
    )
    for parent, has_children in q.all():
        print(parent.name, has_children)

print("Method One")
method_one(session)
print("Method Two")
method_two(session)
print("Method Three")
method_three(session)
