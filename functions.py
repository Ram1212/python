#!/usr/bin/python
#Program for functions pay scale from user input

hrs = raw_input("Enter Hours:")

h = float(hrs)

rate = raw_input("Enter Rate:")

r = float(rate)



def computepay(h,r):

    if (h>40) : 

        pay = (40*r)+(h-40)*1.5*r

    else:

        pay = (h*r)     

    return pay

print computepay(h,r)
