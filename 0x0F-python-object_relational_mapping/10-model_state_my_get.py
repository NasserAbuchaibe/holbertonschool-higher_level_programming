#!/usr/bin/python3
""" ok """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    id_v = session.query(State).filter_by(name=argv[4]).first()
    if id_v:
        print("{}".format(id_v.id))
    else:
        print("Not found")
    session.close()
