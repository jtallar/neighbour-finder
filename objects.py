import math

class Molecule(object):

    def __init__(self, id, x=0, y=0, r=0):
        """Returns a Molecule object with the given coordinates

        Parameters
        ----------
        id : int
            Molecule id
        x : float
            Horizontal coordinate
        y : float
            Vertical coordinate
        r : float
            Molecule radius
        """

        self.id = id
        self.x = x
        self.y = y
        self.r = r

    def center_distance(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

    def border_distance(self, other):
        return self.center_distance(other) - self.r - other.r

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Molecule(%s,%s; r=%s)" % (self.x, self.y, self.r)

    # Define hash and eq methods to allow key usage
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not (self == other)

class MoleculeNode(object):

    def __init__(self, molecule, next=None):
        """Returns a Molecule object with the given coordinates

        Parameters
        ----------
        molecule : Molecule
            Molecule in node
        next : Molecule
            Next molecule in list
        """

        self.molecule = molecule
        self.next = next

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Node{%s, next=%s}" % (self.molecule, self.next)
        
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