# Integral to solve for Jack Straton because of Mathematica fail
# Date: January 18, 2016

from sympy.mpmath import *


def main():
    mp.dps = 64
    pi = .6
    pf = .4
    # Boltzmann constant in Hartrees
    kB  = 3.1668114*10**-6
    # Use Kelvin
    temp = 1500
    g0 = 0.23544264832709902

    while temp < 10000:
      print temp, quad(lambda x: ((e**-x*(g0**2 + 2*kB*temp*x)**3)/(4*sqrt(2)*(kB*temp)**2.5*x**1.5))*(atan((sqrt(2*kB*temp*x)/pf))*atan((sqrt(2*kB*temp*x)/pi))), [0, inf])
      temp += 500




if __name__ == '__main__':
    main()
