import genLib as gen
import sys
import json

if len(sys.argv) > 3:
    print('You have specified too many arguments')
    sys.exit(1)

if len(sys.argv) < 3:
    print('You need to specify number of particles (N) and simulation area side (L)')
    sys.exit(2)

N = int(sys.argv[1])
L = int(sys.argv[2])

# Read configurations from file
with open("filenameConfig.json") as file:
    filename_params = json.load(file)

particles = gen.particles(N, L)
for part in particles:
    print(part)

gen.data_files(N, L, particles, filename_params)