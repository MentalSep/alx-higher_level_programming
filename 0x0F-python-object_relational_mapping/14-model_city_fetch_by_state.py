#!/usr/bin/python3
"""state_fetch_all module"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = Session(engine)
    for city, state in session.query(City, State).filter(
                        State.id == City.state_id).order_by(City.id).all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.commit()
    Session.close()
