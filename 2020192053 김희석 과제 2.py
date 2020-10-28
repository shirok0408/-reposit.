import random
import math
import numpy

A = [0.0, 0.0]
B = [0.0, 0.0]
C = [0.0, 0.0]
d = 0.0
t = 0.0

for i in range(2):
    A[i] = random.randrange(100)
    B[i] = random.randrange(100)
    C[i] = random.randrange(100)

t = numpy.arccos((B[0]*C[0]-A[0]*C[0]+A[0]**2-B[0]*A[0]+B[1]*C[1]+A[1]**2-B[1]*A[1]-C[1]*A[1])/math.sqrt(((A[0]-B[0])**2+(A[1]-B[1])**2)*((A[0]-C[0])**2+(A[1]-C[1])**2)))/numpy.pi*180
d = abs(B[0]*A[1]-B[1]*A[0]-C[0]*A[1]+A[0]*C[1]+B[1]*C[0]-B[0]*C[1])/(math.sqrt((B[0]-C[0])**2+(B[1]-C[1])**2))

print('A:(%d,%d), B:(%d,%d), C:(%d, %d) angle: %f(degree), distance: %f' % (A[0], A[1], B[0], B[1], C[0], C[1], t, d))