#!/usr/bin/python3
"""
Este modulo se conecta con una base de datos.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

    
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    inicio = sessionmaker(bind=engine)
    sesion = inicio()

    states = sesion.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
    
    sesion.close()
    