import numpy as np      # Install numpy
import objects as obj
import random

# Define constants
EMPTY_SPACE = -1

# Simulation area is a square. Its side value is L.
# Passed by file.
L = 100

# The amount of particles is N.
# Passed by file.
N = 10

# The radius for analysis of closeness between particles.
# Input by arguments.
Rc = 0.5

# Matrix is used to represent the entire simulation area divided in MxM zones.
# It is required to be L / M > Rc
# Input by arguments.
M = 4
cell_width = L / M

# Each particle has static and dynamic fields.
# Information passed by file.
# Static fields for particle sub-i. Radius and Property.
Ri = 0.37
Pi = 1

# Dynamic fields. Position and velocity.
PXi = 5.67
PYi = 4.34
PVXi = 0
PVYi = 0

# TODO: Get particle pos from file
(min_coord, max_coord) = (0, L)
head = [None] * (M * M)
for id in range(N):
    (x, y) = (random.uniform(min_coord, max_coord), random.uniform(min_coord, max_coord))
    cell_index = int(x / cell_width) + int(y / cell_width) * M
    # Molecule ids go from 1 to N
    head[cell_index] = obj.MoleculeNode(obj.Molecule(id + 1, x, y), head[cell_index])

# id -> [...]
neighbour_dict = {}

# Output: file with id,neigh1,neigh2,...,neighK
# If id not in file, no neighbours for that id?