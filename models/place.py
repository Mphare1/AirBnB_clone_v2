#!/usr/bin/python3
""" Place Module"""

from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey

association = Table("place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
               primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
               primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay
    """
  
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            place_reviews = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    place_reviews.append(reviews)

            return place_reviews

        @property
        def amenities(self):
            list_amenities = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    list_amenities.append(amenity)

            return list_amenities

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
