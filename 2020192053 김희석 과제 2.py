import random
import math
import numpy

A = [0.0, 0.0]*100
B = [0.0, 0.0]*100
C = [0.0, 0.0]*100
d = [0.0]*100
t = [0.0]*100


for i in range(101):
    A[i] = random.randrange(100)
    B[i] = random.randrange(100)
    C[i] = random.randrange(100)

for i in range(0, 50):
    if B[2*i]==C[2*i] and B[2*i+1]==C[2*i+1]:
        d[i] = math.sqrt((A[2*i]-B[2*i])**2+(A[2*i+1]-B[2*i+1])**2)
        t[i] = numpy.arccos((B[2*i]*C[2*i]-A[2*i]*C[2*i]+A[2*i]**2-B[2*i]*A[2*i]+B[2*i+1]*C[2*i+1]+A[2*i+1]**2-B[2*i+1]*A[2*i+1]-C[2*i+1]*A[2*i+1])/math.sqrt(((A[2*i]-B[2*i])**2+(A[2*i+1]-B[2*i+1])**2)*((A[2*i]-C[2*i])**2+(A[2*i+1]-C[2*i+1])**2)))/numpy.pi*180
    if A[2*i]==C[2*i] and A[2*i+1]==C[2*i+1]:
        t[i] = 0
    if B[2*i]==A[2*i] and B[2*i+1]==A[2*i+1]:
        t[i] = 0
    else:
        t[i] = numpy.arccos((B[2*i]*C[2*i]-A[2*i]*C[2*i]+A[2*i]**2-B[2*i]*A[2*i]+B[2*i+1]*C[2*i+1]+A[2*i+1]**2-B[2*i+1]*A[2*i+1]-C[2*i+1]*A[2*i+1])/math.sqrt(((A[2*i]-B[2*i])**2+(A[2*i+1]-B[2*i+1])**2)*((A[2*i]-C[2*i])**2+(A[2*i+1]-C[2*i+1])**2)))/numpy.pi*180
        d[i] = abs(B[2*i]*A[2*i+1]-B[2*i+1]*A[2*i]-C[2*i]*A[2*i+1]+A[2*i]*C[2*i+1]+B[2*i+1]*C[2*i]-B[2*i]*C[2*i+1])/(math.sqrt((B[2*i]-C[2*i])**2+(B[2*i+1]-C[2*i+1])**2))

for i in range(0, 50):
    print('A:(%d,%d), B:(%d,%d), C:(%d, %d) angle: %f(degree), distance: %f' % (A[2*i], A[2*i+1], B[2*i], B[2*i+1], C[2*i], C[2*i+1], t[i], d[i]))
