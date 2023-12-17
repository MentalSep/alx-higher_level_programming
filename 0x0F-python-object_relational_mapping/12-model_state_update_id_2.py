#!/usr/bin/python3
"""state_fetch_all module"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = Session(engine)
    new = session.query(State).get(2)
    new.name = 'New Mexico'
    session.commit()
    Session.close()
