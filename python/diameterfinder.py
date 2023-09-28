import numpy

pi = numpy.pi
numsquared = 0

while True:
    num = int(input('\nRadius of circle: '))
    numsquared = num*num
    area = numsquared*pi
    print('Area of circle is: ' + str(area))
    