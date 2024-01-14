#!/usr/bin/python3
"""
Este modulo se conecta con una base de datos.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

    
if __name__ == "__main__":
    """
    Realiza una consulta para buscar un valor en especifico.

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    inicio = sessionmaker(bind=engine)
    sesion = inicio()

    states = sesion.query(State).filter_by(id = 2).first()

    if states:
        states.name = "New Mexico"
        sesion.commit

    sesion.close()
    