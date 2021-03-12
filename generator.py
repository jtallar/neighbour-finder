import random
import objects as obj

R = 0.5
def particles(n, side):
    part = []
    for _ in range(n):
        point = obj.Point(random.uniform(0, side), random.uniform(0, side))
        part.append(obj.Particle(point, R, 'green'))
    return part


#TODO: Generate dynamic and static files, reading N and L from arg
def data_files(n, side, particles):
    static_file = open("static.txt", "w")
    static_file.write(str(n))
    static_file.write('\n')
    static_file.write(str(side))
    for p in particles:
        static_file.write('\n')
        static_file.write(str(p.radius))
        static_file.write(' ')
        static_file.write(p.property)
    static_file.close()

    dynamic_file = open("dynamic.txt", "w")
    dynamic_file.write('0')       # dynamic time
    for p in particles:
        dynamic_file.write('\n')
        dynamic_file.write(str(round(p.point.x, 3)))
        dynamic_file.write(' ')
        dynamic_file.write(str(round(p.point.y, 3)))
    dynamic_file.close()
