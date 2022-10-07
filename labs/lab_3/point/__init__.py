"""
Write the definition of a Point class. Objects from this class should have the 
following members:
- x and y coordinates.
- a method show to display the coordinates of the point
- a method move to change these coordinates in the direction x or/and y.
- a method dist that computes the distance between 2 points.
Also write a main function to test your implementation.
"""

from __future__ import annotations
import numpy as np


class Point:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point: ({self.x}, {self.y})"

    def __sub__(self, other: Point) -> float:
        return np.hypot((self.x - other.x), (self.y - other.y)).astype(float)
