import genLib as gen
import sys
import json

if len(sys.argv) != 3:
    print('Wrong number of args!\nYou need to specify number of particles (N) and simulation area side (L).\nMust run with\n\tpython3 generator.py N L')
    sys.exit(1)

N = int(sys.argv[1])
L = int(sys.argv[2])

# Read configurations from file
with open("filenameConfig.json") as file:
    filename_params = json.load(file)

particles = gen.particles(N, L)
for part in particles:
    print(part)

gen.data_files(N, L, particles, filename_params)