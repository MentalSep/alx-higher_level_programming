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
    result = session.query(State).filter(State.name == (sys.argv[4],))
    print(result.id if result else "Not found")
    Session.close()
