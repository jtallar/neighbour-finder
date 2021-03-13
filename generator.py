import genLib as gen
import sys
import json

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print('Wrong number of args!\nYou need to specify number of particles (N), simulation area side (L) and (optionally) particle radius (if not, random from 0 to 1).\nMust run with\n\tpython3 generator.py N L [rp]')
    sys.exit(1)

N = int(sys.argv[1])
if N <= 0:
    print('Number of particles N must be positive!')
    sys.exit(1)

L = int(sys.argv[2])
if L <= 0:
    print('Area side L must be positive!')
    sys.exit(1)

rad = None
if len(sys.argv) == 4:
    rad = float(sys.argv[3])
    if rad < 0:
        print('Particle radius must be positive or cero!')
        sys.exit(1)

# Read configurations from file
with open("filenameConfig.json") as file:
    filename_params = json.load(file)

particles = gen.particles(N, L, rad)
for part in particles:
    print(part)

gen.data_files(N, L, particles, filename_params)