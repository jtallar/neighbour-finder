class Particle(object):

    def __init__(self, point, radius, prop):
        self.point = point
        self.radius = radius
        self.property = prop

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return " (%s,%s) ~ R: %s ~ %s" % (round(self.point.x, 3), round(self.point.y, 3), self.radius, self.property)

# Point with positive coordinates
# (0,0) is at top left corner
class Point(object):

    def __init__(self, x=0, y=0):
        """Returns a Point object with the given coordinates

        Parameters
        ----------
        x : int
            Horizontal coordinate
        y : int
            Vertical coordinate
        """
        self.x = x
        self.y = y

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "(%s,%s)" % (round(self.x, 3), round(self.y, 3))

    # Define hash and eq methods to allow key usage
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not (self == other)