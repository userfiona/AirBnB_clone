#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel

from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Return dictionary representation of State."""
        state_dict = super().to_dict()
        state_dict['name'] = self.name
        return state_dict

    @classmethod
    def from_dict(cls, data_dict):
        """Create State object from dictionary."""
        return cls(**data_dict)`
