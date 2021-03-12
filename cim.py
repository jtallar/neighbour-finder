import numpy as np      # Install numpy
import objects as obj
import random
import math

# Simulation area is a square. Its side value is L.
# Passed by file.
L = 100

# The amount of particles is N.
# Passed by file.
N = 20

# The radius for analysis of closeness between particles.
# Input by arguments.
Rc = 20

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

# State whether to read or not periodically
periodic_cells = True

# [M+2][M+1], posta en [1 a M][1 a M]
#   3    0   1   2   3
#   15  |12  13  14  15
#   11  |8   9   10  11     --> X=[X / M + 1][X % M + 1]
#   7   |4   5   6   7      --> 4=[2][1], 5=[2][2]
#   3   |0   1   2   3      --> 0=[1][1], 1=[1][2]
#   15   12  13  14  15
# ^ 
# y, x -->

# TODO: Get particle pos from file
(min_coord, max_coord) = (0, L)
part = [(69.78,64.23),(71.10,36.66),(71.70,28.38),(2.46,25.76),(92.59,46.57),(65.41,5.32),(76.89,61.07),(84.55,15.98),(44.61,35.58),(15.88,71.86),(50.59,65.66),(18.67,99.61),(81.27,22.87),(52.95,13.96),(89.02,63.58),(69.69,8.60),(20.46,80.11),(48.49,44.08),(4.03,13.31),(23.20,5.13)]

head_matrix = np.full((M + 2, M + 1), None)
for id in range(N):
    # (x, y) = (random.uniform(min_coord, max_coord), random.uniform(min_coord, max_coord))
    (x, y) = part[id]
    cell_index = int(x / cell_width) + int(y / cell_width) * M
    (row, col) = (int(cell_index / M + 1), int(cell_index % M + 1))
    # Molecule ids go from 1 to N
    head_matrix[row][col] = obj.MoleculeNode(obj.Molecule(id + 1, x, y), head_matrix[row][col])
    # If periodic cells off, skip
    if not periodic_cells:
        continue
    # Copy to repeated position if needed
    if row == 1:
        head_matrix[-1][col] = obj.MoleculeNode(obj.Molecule(id + 1, x, y + L), head_matrix[-1][col])
    elif row == M:
        head_matrix[0][col] = obj.MoleculeNode(obj.Molecule(id + 1, x, y - L), head_matrix[0][col])
    if col == M:
        head_matrix[row][0] = obj.MoleculeNode(obj.Molecule(id + 1, x - L, y), head_matrix[row][0])
        if row == 1:
            head_matrix[-1][0] = obj.MoleculeNode(obj.Molecule(id + 1, x - L, y + L), head_matrix[-1][0])
        elif row == M:
            head_matrix[0][0] = obj.MoleculeNode(obj.Molecule(id + 1, x - L, y - L), head_matrix[0][0])

neighbour_list = [set() for index in range(N)]
for cell in range(M * M):
    (row, col) = (int(cell / M + 1), int(cell % M + 1))
    # Iterate cell over itself
    cell_cur = head_matrix[row][col]
    while cell_cur:
        next_cell_cur = cell_cur.next
        while next_cell_cur:
            if cell_cur.molecule.border_distance(next_cell_cur.molecule) < Rc:
                # Id goes from 1 to N, index in list goes from 0 to N-1
                neighbour_list[cell_cur.molecule.id - 1].add(next_cell_cur.molecule.id)
                neighbour_list[next_cell_cur.molecule.id - 1].add(cell_cur.molecule.id)
            next_cell_cur = next_cell_cur.next
        cell_cur = cell_cur.next
    
    # Iterate over 3 neighbours --> L` --> DOWN, DOWN-LEFT, LEFT, UP-LEFT
    for other_row, other_col in [(row -1, col), (row - 1, col - 1), (row, col - 1), (row + 1, col - 1)]:
        cell_cur = head_matrix[row][col]
        while cell_cur:
            next_cell_cur = head_matrix[other_row][other_col]
            while next_cell_cur:
                if cell_cur.molecule.border_distance(next_cell_cur.molecule) < Rc:
                    # Id goes from 1 to N, index in list goes from 0 to N-1
                    neighbour_list[cell_cur.molecule.id - 1].add(next_cell_cur.molecule.id)
                    neighbour_list[next_cell_cur.molecule.id - 1].add(cell_cur.molecule.id)
                next_cell_cur = next_cell_cur.next
            cell_cur = cell_cur.next

out_file = open("out.txt", 'w')
id = 1
for neighbour_set in neighbour_list:
    ids_string = ','.join(str(s) for s in neighbour_set)
    print(f'{id}->{ids_string}', file=out_file)
    id += 1
out_file.close()