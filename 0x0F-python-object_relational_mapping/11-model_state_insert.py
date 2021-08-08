#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    state = session.query(State).filter_by(name='Louisiana').first()
    print(state.id)
    
    session.close()
