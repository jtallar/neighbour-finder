import sys
import json

WHITE = ' 255 255 255'
GREEN = ' 0 255 0'
RED = ' 255 0 0'
C = '1e-10 '

# Read configurations from file
with open("filenameConfig.json") as file:
    filename_params = json.load(file)

if len(sys.argv) > 2:
    print('You have specified too many arguments')
    sys.exit(1)

if len(sys.argv) < 2:
    print('You need to specify id of particle selected')
    sys.exit(2)

id = int(sys.argv[1])

dynamic_file = open(filename_params["dynamic_file"], "r")
dynamic_file.readline()

static_file = open(filename_params["static_file"], "r")
N = int(static_file.readline())
L = float(static_file.readline())
# static_file.close()

if id > N or id < 0:
    print('Particle id must be a number between 0 and', N)
    sys.exit(3)

neighbours_file = open(filename_params["output_neighbours_file"], "r")
lines = neighbours_file.read().split('\n')
neighbours_file.close()
print(lines[id-1])
neigh = lines[id-1].split('>')[1].split(',')

ovito_file = open(filename_params["ovito_xyz_file"], "w")
ovito_file.write(str(N+4))
corners = '\n\n'+C+'0 0'+WHITE+'\n'+C+'0 '+str(L)+WHITE+'\n'+C+str(L)+' 0'+WHITE+'\n'+C+str(L)+' '+str(L)+WHITE
ovito_file.write(corners)

for i in range(N):
    line = dynamic_file.readline().split(' ')
    (x,y,r) = (line[0]+' ', line[1]+' ', static_file.readline().split()[0]+' ')
    if str(i+1) in neigh:
        color = GREEN
    elif i+1 == id:
        color = RED
    else: 
        color = WHITE
    ovi_line = '\n'+r+x+y+color
    ovito_file.write(ovi_line)

dynamic_file.close()
static_file.close()
ovito_file.close()
    
# particle_radius = []
# for line in neighbours_file:
#     rad = int(line.split()[0]) # Ignoring particle property
#     particle_radius.append(rad)
#     # Save top two radius
#     if rad > two_max_radius[0]:
#         two_max_radius.pop(0)
#         two_max_radius.append(rad)
#         two_max_radius.sort()

# static_file.close()