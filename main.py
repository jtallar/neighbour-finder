import generator as gen
import sys

# Simulation area is a square. Its side value is L.
# Passed by file.
L = 100

# The amount of particles is N.
# Passed by file.
N = 100

# The radius for analysis of closeness between particles.
# Input by arguments.
Rc = 0.5

# Matrix is used to represent the entire simulation area divided in MxM zones.
# It is required to be L / M > Rc
# Input by arguments.
M = 5

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

####################################################33


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