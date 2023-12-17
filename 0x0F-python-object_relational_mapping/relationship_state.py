#!/usr/bin/python3
"""the model_state module"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """the State class"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128),  nullable=False)
    cities = relationship('City', cascade="all, delete", backref="state")
