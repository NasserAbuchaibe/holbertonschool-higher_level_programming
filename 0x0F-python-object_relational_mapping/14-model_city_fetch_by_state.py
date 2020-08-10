#!/usr/bin/python3
""" ok """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for cty in session.query(City).join(State).order_by(City.id).all():
        print("{}: ({}) {}".format(cty.state.name, cty.id, cty.name))
    session.close()
