#!/usr/bin/python3
"""the model_city module"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City (Base):
    """the City class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
