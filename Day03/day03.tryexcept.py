# try/except
a = 'Good Morning'
try: # if things work out, do this
    x = int(a)
except: # if don't, do this
    x = 'string'
print('First', x)


b = '123'
try:
    y = int(b)
except:
    y = 'string'
print('Second', y)


c = input('Enter a number:')
try:
    x = int(c)
except:
    x = 0

if x > 0:
    print('Good job')
else:
    print('This is not a number dude')


# Write a program to input hours and rate per hour to compute gross pay.
"""Pay the hourly rate for the hours up to 40 and 1.5times the hourly rate for above 40 hours.
Use 45 hours and rate of 10.5 per hour and the gross pay should be 498.75"""
hrs = input("Enter Hours: ")
rate = input("Enter Rates: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error")

if h > 40:
    reg = h * r
    over = (h-40) * r * 0.5
    p = reg + over
else:
    p = h * r
print(p)
print('Good work')