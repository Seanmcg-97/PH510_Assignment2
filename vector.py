#!/bin/python3
"""
This program is used to orientate and manipulate objects of Cartesian
and spherical polar coordinates in a parent and child class
"""
import numpy as np

class Vector:
    """
    Vector class for 3-D cartesian quantities
    """
    def __init__(self, a, b, c):
        """
        Function to initiate coordinates in Vector
        """
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        """
        Assumes floating poit when printing
        """
        return f"Vector: ({self.a:.2f}, {self.b:.2f}, {self.c:.2f})"

    def __add__(self, other):
        """
        Overloads addition for the elements of two instances
        """
        return Vector(self.a + other.a, self.b + other.b, self.c + other.c)

    def __sub__(self, other):
        """
        Performs subtraction between the elements of two instances
        """
        return Vector(self.a - other.a, self.b - other.b, self.c - other.c)

    def __dot_product__(self, other):
        """
        Function to perform dot product calculation A.B
        """
        return self.a * other.a + self.b * other.b + self.c * other.c

    def __cross_product__(self, other):
        """
        Function to perform cross product calculation AxB
        """
        return (self.b*other.c - self.c*other.b, self.c*other.a - self.a*other.c,self.a*other.b - self.b*other.a)

    def __mag__(self):
        """
        Function to find the magnitude |A|
        """
        return np.sqrt(self.a**2 + self.b**2 + self.c**2)

    def __area__(self, other):
        """
        Function to find the area of a triangle between 2 vectors
        """
        area = 0.5*(np.sqrt((self.b*other.c - self.c*other.b)**2 + (self.c*other.a - self.a*other.c)**2 + (self.a*other.b - self.b*other.a)**2))
        return area

    def __angle__(self, other):
        """
        Function to calculate angle between 2 vectors
        """
        angle = ( 180 * np.arccos((self.a * other.a + self.b * other.b + self.c * other.c)/((np.sqrt(self.a**2+self.b**2+self.c**2))*(np.sqrt(other.a**2+other.b**2+other.c**2))))/np.pi)
        return angle

class VectorP(Vector):
    """
    Vector class for 3-D cartesian quantities
    """
    def __init__(self, r, t, p):
        Vector.__init__(self, r * np.sin(p) * np.cos(t), r * np.sin(p) * np.sin(t), r * np.cos(p))

    def __str__(self):
        """
        Assumes floating poit when printing
        """
        r = np.sqrt((self.a)**2 + (self.b)**2 + (self.c)**2)
        t = np.arccos(self.c/np.sqrt((self.a)**2 + (self.b)**2 + (self.c)**2))

        #Licensing provided in LICENSE.txt file
        p = np.arctan2(self.b, self.a)

        return f"Vector: ({r:.6f}, {t:.6f}, {p:.6f})"

#License 

