import numpy as np      # Install numpy
import objects as obj
import random
import math
import generator as gen
import sys

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
Rc = 20

# Matrix is used to represent the entire simulation area divided in MxM zones.
# It is required to be L / M > Rc
# Input by arguments.
M = 4
cell_width = L / M
n_blocks = M * M

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

####################################################


if len(sys.argv) > 3:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 3:
    print('You need to specify number of particles (N) and simulation area side (L)')
    sys.exit()

N = int(sys.argv[1])
L = int(sys.argv[2])

particles = gen.particles(N, L)
for part in particles:
    print(part)

gen.data_files(N, L, particles)

################################################

# State whether to read or not periodically
periodic_cells = True

# TODO: Get particle pos from file
(min_coord, max_coord) = (0, L)
head = [None] * (n_blocks)
for id in range(N):
    (x, y) = (random.uniform(min_coord, max_coord), random.uniform(min_coord, max_coord))
    cell_index = int(x / cell_width) + int(y / cell_width) * M
    # Molecule ids go from 1 to N
    head[cell_index] = obj.MoleculeNode(obj.Molecule(id + 1, x, y), head[cell_index])

print(head)
# TODO: What if M <= 2?
# id -> [...]
# Im in cell X (%4 != 0) -> X, X-M, X-1, X+M-1, X+M-1
# Im in cell X (%4 == 0) -> X, X-M, X-1, X+M-1, X+2M-1
# Take num % (n_blocks)
# If !periodic_cells -> (%4 == 0) -> Read X and X-M
#                       All -> Skip < 0 and >= n_blocks
neighbour_list = [[]] * N
print(neighbour_list)
for cell in range(n_blocks):
    # Iterate over itself
    cell_cur = head[cell]
    while cell_cur:
        next_cell_cur = cell_cur.next
        while next_cell_cur:
            if cell_cur.molecule.border_distance(next_cell_cur.molecule) < Rc:
                neighbour_list[cell_cur.molecule.id - 1].append(next_cell_cur.molecule.id)
            next_cell_cur = next_cell_cur.next
        cell_cur = cell_cur.next

    indexes = [cell - M]
    if periodic_cells or cell % 4 != 0:
        indexes.extend([cell - 1, cell + M - 1, (cell + 2 * M - 1) if (cell % 4 == 0) else (cell + M - 1)])
    
    # Iterate over 4 neighbour cells
    for i in indexes:
        if not periodic_cells and (i < 0 or i >= n_blocks):
            continue
        # Iterate over cell in indexes
        cell_cur = head[cell]
        while cell_cur:
            next_cell_cur = head[i % n_blocks]
            while next_cell_cur:
                if cell_cur.molecule.border_distance(next_cell_cur.molecule) < Rc:
                    neighbour_list[cell_cur.molecule.id - 1].append(next_cell_cur.molecule.id)
                next_cell_cur = next_cell_cur.next
            cell_cur = cell_cur.next

print(neighbour_list)

# Output: file with id,neigh1,neigh2,...,neighK
# If id not in file, no neighbours for that id?