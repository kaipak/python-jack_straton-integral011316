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
    # Summation limit
    ifny = 25

    #print analytical(pi, pf, kB, temp, g0)
    # print numerical(pi, pf, kB, temp, g0, ifny)
    # print hyper_test(ifny, pi, pf)
    #print hyper_test(2, 2.25)
    #print my_hyper([-1,-1.5,.5,1],[-.5,-1,1.5],2.25)
    print hyper([-1,-1.5,.5,1],[-.5,-1,1.5],2.25)

def analytical(pi, pf, kB, temp, g0):
    return quad(lambda x: ((e**-x*(g0**2 + 2*kB*temp*x)**3)/(4*sqrt(2)
                           *(kB*temp)**2.5*x**1.5))*(atan((sqrt(2*kB*temp*x)/pf))
                           *atan((sqrt(2*kB*temp*x)/pi))), [0, inf])

def numerical(pi, pf, kB, temp, g0, ifny):
    return nsum(lambda n: ((g0**6 + 2*kB*(.5 + n)*temp*(3*g0**4 + kB*(3 + 2*n)
                           *temp*(kB*(5 + 2*n)*temp + 3 * g0**2)))
                           *gamma(.5 + n)
                           *((-2*kB*temp)/pi**2)**n*rf(.5,n)*rf(1,n)
                           *hyper([-n, -.5-n, .5, 1], [.5-n,-n,1.5],pi**2/pf**2))
                           /(fac(n)*rf(1.5,n)), [1,ifny])

# Include some conditionals to handle weird cases that Sympy doesn't appear to
# know about
#
def my_hyper(a,b,z):
    a_zeros = 0
    b_zeros = 0

    for num in a:
        if num == 0:
            a_zeros += 1
    for num in b:
        if num == 0:
            b_zeros += 1

    if a_zeros >= b_zeros and (a_zeros != 0 and b_zeros != 0):
        return 1

    return hyper(a, b, z)

def hyper_test(ifny, z):
    return nsum(lambda n: (my_hyper([-n,-.5-n,.5,1],[.5-n,-n,1.5],z)), [0,ifny])

if __name__ == '__main__':
    main()
