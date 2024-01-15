#!/usr/bin/python3
"""
Este modulo se conecta con una base de datos.
"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    
    name = Column(String(128),
                  nullable=False)
    
    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False,)
    
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa',
                           pool_pre_ping=True)
