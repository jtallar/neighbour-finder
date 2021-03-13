import objects as obj
import json
import sys
import time

if len(sys.argv) != 3:
    print('Wrong number of args!\nYou need to specify interaction radio (Rc) and edge periodic condition (periodic or not_periodic).\nMust run with\n\tpython3 bruteForce.py Rc (periodic|not_periodic)')
    sys.exit(1)

# The radius for analysis of closeness between particles.
Rc = float(sys.argv[1])
if Rc < 0:
    print('Interaction radio Rc must be positive!')
    sys.exit(1)

# State whether to read or not periodically.
if sys.argv[2] != 'periodic' and sys.argv[2] != 'not_periodic':
    print('Edge periodic condition must be given with periodic or not_periodic!')
    sys.exit(1)
periodic_cells = (sys.argv[2] == 'periodic')

# Read configurations from file
with open("filenameConfig.json") as file:
    filename_params = json.load(file)

dynamic_file = open(filename_params["dynamic_file"], "r")
# First time in file.
cur_time = float(dynamic_file.readline())

static_file = open(filename_params["static_file"], "r")
# The amount of particles is N.
N = int(static_file.readline())
# Simulation area is a square. Its side value is L.
L = float(static_file.readline())

# Start chronometer
start_time = time.time()

# Will iteratively read lines for each particle sub-i
# Dynamic fields for particle sub-i. Position and speed as  xi yi vxi vyi
# Static fields for particle sub-i. Radius and Property as  ri pi. Properties not used
particles = []
for id in range(N):
    (x, y, vx, vy) = [float(i) for i in dynamic_file.readline().split()]
    rad = float(static_file.readline().split()[0])
    particles.append(obj.Molecule(id + 1, x, y, rad))

dynamic_file.close()
static_file.close()

def generic_border_distance(periodic, mol_1, mol_2, side=None):
    if periodic:
        return mol_1.multidir_border_distance(mol_2, side)
    return mol_1.border_distance(mol_2)

neighbour_list = [set() for index in range(N)]
for first in range(0, N):
    for second in range(first + 1, N):
        if generic_border_distance(periodic_cells, particles[first], particles[second], L) < Rc:
            # Id goes from 1 to N, index in list goes from 0 to N-1
            neighbour_list[particles[first].id - 1].add(particles[second].id)
            neighbour_list[particles[second].id - 1].add(particles[first].id)        

end_time = time.time()
print(f'Brute Force Execution time \t ⏱  {end_time - start_time} seconds')

with open(filename_params["output_neighbours_file"], 'w') as out_file:
    id = 1
    for neighbour_set in neighbour_list:
        ids_string = ','.join(str(s) for s in neighbour_set)
        print(f'{id}->{ids_string}', file=out_file)
        id += 1
    print(f'Wrote output at {filename_params["output_neighbours_file"]}')