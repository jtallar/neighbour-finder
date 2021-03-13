import objects as obj
import random

MAX_RADIUS = 1
# TODO: En un futuro, deberíamos chequear que no haya superposición con ninguna otra partícula, 
# que la distancia entre centros sea menor a la suma de sus radios. 
# Podría ponerse que si en "1000 veces" no pudo poner partícula por superposición, cortar porque no hay lugares.
def particles(n, side, rad):
    part = []
    for i in range(n):
        part.append(obj.Molecule(i + 1, random.uniform(0, side), random.uniform(0, side), rad if rad else random.uniform(0, MAX_RADIUS)))
    return part

# TODO: Check rounding to 4 decimals.
#Generate dynamic and static files, reading N and L from arg
def data_files(n, side, particles, filename_json):
    static_file = open(filename_json["static_file"], "w")
    static_file.write(str(n))
    static_file.write('\n')
    static_file.write(str(side))
    for p in particles:
        static_file.write('\n')
        static_file.write(str(round(p.r, 4)))
        static_file.write(' ')
        static_file.write(p.prop)
    static_file.close()

    dynamic_file = open(filename_json["dynamic_file"], "w")
    dynamic_file.write('0')       # dynamic time
    for p in particles:
        dynamic_file.write('\n')
        dynamic_file.write(str(round(p.x, 4)))
        dynamic_file.write(' ')
        dynamic_file.write(str(round(p.y, 4)))
        dynamic_file.write(' ')
        dynamic_file.write(str(0)) # Vx
        dynamic_file.write(' ')
        dynamic_file.write(str(0)) # Vy
    dynamic_file.close()
