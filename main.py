# Integral to solve for Jack Straton because of Mathematica fail
# Date: January 18, 2016

from sympy.mpmath import *


def main():
    mp.dps = 32
    pi = .6
    pf = .4
    # Boltzmann constant in Hartrees
    kB  = 3.1668114**-6
    temp = 1500
    g0 = 0.23544264832709902


    # Use Kelvin
    print quad(lambda x: ((exp(-x)*(g0**2 + 2*kB*temp*x)**3)/(4*sqrt(2)*(kB*temp)**2.5*x**1.5))\
                          *atan((sqrt(2*kB*temp*x)/pf))*atan((sqrt(2*kB*temp*x)/pi)), [0, inf])




if __name__ == '__main__':
    main()
