import numpy as np      # Install numpy
import objects as obj
import random
import math
import json
import sys

# Read configurations from file
with open("config.json") as file:
    general_params = json.load(file)

dynamic_file = open(general_params["dynamic_file"], "r")
# First time in file.
cur_time = float(dynamic_file.readline())

static_file = open(general_params["static_file"], "r")
# The amount of particles is N.
N = int(static_file.readline())
# Simulation area is a square. Its side value is L.
L = float(static_file.readline())

# The radius for analysis of closeness between particles.
# Input by arguments.
Rc = 20

# Matrix is used to represent the entire simulation area divided in MxM zones.
# It is required to be L / M > Rc
# Input by arguments.
M = 4
cell_width = L / M

# State whether to read or not periodically.
# Input by arguments.
periodic_cells = True

# Will iteratively read lines for each particle sub-i
# Dynamic fields for particle sub-i. Position and speed as  xi yi vxi vyi
# Static fields for particle sub-i. Radius and Property as  ri pi. Properties not used

# [M+2][M+1], real points in [1:M][1:M]
#   3    0   1   2   3
#   15  |12  13  14  15
#   11  |8   9   10  11     --> X=[X / M + 1][X % M + 1]
#   7   |4   5   6   7      --> 4=[2][1], 5=[2][2]
#   3   |0   1   2   3      --> 0=[1][1], 1=[1][2]
#   15   12  13  14  15
# ^ 
# y, x -->

# Top two radius will be saved to ensure condition applies correctly.
two_max_radius = [0, 0]

head_matrix = np.full((M + 2, M + 1), None)
for id in range(N):
    (x, y) = [float(i) for i in dynamic_file.readline().split()] # TODO: When speed added to generator.py, write (x, y, vx, vy) = ...
    rad = float(static_file.readline().split()[0]) # Ignoring particle property
    # Save top two radius
    if rad > two_max_radius[0]:
        two_max_radius.pop(0)
        two_max_radius.append(rad)
        two_max_radius.sort()

    cell_index = int(x / cell_width) + int(y / cell_width) * M
    (row, col) = (int(cell_index / M + 1), int(cell_index % M + 1))
    # Molecule ids go from 1 to N
    head_matrix[row][col] = obj.MoleculeNode(obj.Molecule(id + 1, x, y, rad), head_matrix[row][col])
    # If periodic cells off, skip
    if not periodic_cells:
        continue
    # Copy to repeated position if needed
    if row == 1:
        head_matrix[-1][col] = obj.MoleculeNode(obj.Molecule(id + 1, x, y + L, rad), head_matrix[-1][col])
    elif row == M:
        head_matrix[0][col] = obj.MoleculeNode(obj.Molecule(id + 1, x, y - L, rad), head_matrix[0][col])
    if col == M:
        head_matrix[row][0] = obj.MoleculeNode(obj.Molecule(id + 1, x - L, y, rad), head_matrix[row][0])
        if row == 1:
            head_matrix[-1][0] = obj.MoleculeNode(obj.Molecule(id + 1, x - L, y + L, rad), head_matrix[-1][0])
        elif row == M:
            head_matrix[0][0] = obj.MoleculeNode(obj.Molecule(id + 1, x - L, y - L, rad), head_matrix[0][0])

dynamic_file.close()
static_file.close()

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

with open(general_params["output_file"], 'w') as out_file:
    id = 1
    for neighbour_set in neighbour_list:
        ids_string = ','.join(str(s) for s in neighbour_set)
        print(f'{id}->{ids_string}', file=out_file)
        id += 1