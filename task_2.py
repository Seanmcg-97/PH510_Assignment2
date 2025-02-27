#!/bin/python3

import numpy as np
import math

class Vector_p:
    def __init__(self, r, t, p):
        self.x = r * math.sin(p) * math.cos(t)
        self.y = r * math.sin(p) * math.sin(t)
        self.z = r * math.cos(p)

        return f"Vector: ({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    def __str__(self):
        """
        Assumes floating poit when printing
        """
        return f"Vector: ({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    def __add__(self, other):
        """
        Overloads addition for the elements of two instances
        """
        return Vector_p(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector_p(self.x - other.x, self.y - other.y, self.z - other.z)

    def __dot_product__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __Mag__(self, other):
        return np.sqrt(self.x * self.y * self.z + other.x * other.y * other.z)

