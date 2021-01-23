from sqlalchemy import create_engine, Column, Integer, Boolean, Enum, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()

class User(Base):
    """
    Represents a Discord/Minecraft pair

    Attributes
    ----------
    id : int
        Discord ID for the user
    guild : int
        Discord ID of the guild this pair belongs to
    mc_name : String
        User's Minecraft Username
    mc_status : boolean
        Current allowlist status of the user
    """

    id = Column(Integer, primary_key=True)
    guild = Column(Integer)
    mc_name = Column(String(32))
    mc_status = Column(Boolean, default=False)