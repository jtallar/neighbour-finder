import math

class Molecule(object):

    def __init__(self, id, x=0, y=0, r=0, prop='oval'):
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
        self.prop = prop

    def center_distance(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

    def border_distance(self, other):
        return self.center_distance(other) - self.r - other.r

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Molecule %s(%.2f,%.2f; r=%.2f)" % (self.id, self.x, self.y, self.r)

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