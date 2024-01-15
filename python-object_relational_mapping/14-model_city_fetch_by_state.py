#!/usr/bin/python3
"""
Este modulo se conecta con una base de datos.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State
from model_city import Base, City

    
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

    cities = sesion.query(City, State).filter(State.id == City.state_id). all()

    for citie, state in cities:
        print("{}: ({}) {}".format(state.name, citie.id, citie.name))

    sesion.commit()
    sesion.close()
    