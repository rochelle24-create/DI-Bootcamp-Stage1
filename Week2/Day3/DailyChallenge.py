# Instructions
# The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.



# Abilities of a Circle Instance
# Your Circle class should be able to:

# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.
############################################################################################################################

import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle(radius={self.radius}, area={self.area():.2f})"
    
    def __repr__(self):
        return f"Circle({self.radius})"
    
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self.radius + other.radius)
    
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.area() > other.area()
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return math.isclose(self.radius, other.radius)
    
    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.area() < other.area()
    
    def __le__(self, other):
        return self.area() <= other.area() if isinstance(other, Circle) else NotImplemented
    
    def __ge__(self, other):
        return self.area() >= other.area() if isinstance(other, Circle) else NotImplemented
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(round(self.radius, 10))
