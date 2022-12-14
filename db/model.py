from sqlalchemy import Column, ForeignKey, String, Float
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import relationship
from db.database import ORMBase


class OrderTable(ORMBase):
    __tablename__ = "order_log"
    event_id = Column(String, ForeignKey("event_log.event_id"), primary_key=True, unique=True)
    order_id = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    currency = Column(String, nullable=False)


class EventTable(ORMBase):
    __tablename__ = "event_log"
    event_id = Column(String, primary_key=True, unique=True, nullable=False)
    user_id = Column(String, nullable=False)
    event = Column(String, nullable=False)
    event_datetime = Column(DATETIME(fsp=3), nullable=False)
    order = relationship("OrderTable", backref="order_log")
