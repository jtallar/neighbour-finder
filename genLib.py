import objects as obj
import random

MAX_RADIUS = 1
def particles(n, side):
    part = []
    for i in range(n):
        part.append(obj.Molecule(i, random.uniform(0, side), random.uniform(0, side), random.uniform(0, MAX_RADIUS)))
    return part


#Generate dynamic and static files, reading N and L from arg
def data_files(n, side, particles):
    static_file = open("static.txt", "w")
    static_file.write(str(n))
    static_file.write('\n')
    static_file.write(str(side))
    for p in particles:
        static_file.write('\n')
        static_file.write(str(p.r))
        static_file.write(' ')
        static_file.write(p.prop)
    static_file.close()

    dynamic_file = open("dynamic.txt", "w")
    dynamic_file.write('0')       # dynamic time
    for p in particles:
        dynamic_file.write('\n')
        dynamic_file.write(str(round(p.x, 3)))
        dynamic_file.write(' ')
        dynamic_file.write(str(round(p.y, 3)))
    dynamic_file.close()
