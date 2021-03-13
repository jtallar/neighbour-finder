import objects as obj
import random

MAX_RADIUS = 1
def particles(n, side):
    part = []
    for i in range(n):
        part.append(obj.Molecule(i + 1, random.uniform(0, side), random.uniform(0, side), random.uniform(0, MAX_RADIUS)))
    return part


#Generate dynamic and static files, reading N and L from arg
def data_files(n, side, particles, filename_json):
    static_file = open(filename_json["static_file"], "w")
    static_file.write(str(n))
    static_file.write('\n')
    static_file.write(str(side))
    for p in particles:
        static_file.write('\n')
        static_file.write(str(p.r))
        static_file.write(' ')
        static_file.write(p.prop)
    static_file.close()

    dynamic_file = open(filename_json["dynamic_file"], "w")
    dynamic_file.write('0')       # dynamic time
    for p in particles:
        dynamic_file.write('\n')
        dynamic_file.write(str(round(p.x, 3)))
        dynamic_file.write(' ')
        dynamic_file.write(str(round(p.y, 3)))
        dynamic_file.write(' ')
        dynamic_file.write(str(0)) # Vx
        dynamic_file.write(' ')
        dynamic_file.write(str(0)) # Vy
    dynamic_file.close()
