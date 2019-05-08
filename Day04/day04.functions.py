# built-in function lists
"""float(), type(), int(), input(), """

# def doesn't invoke automatically
x = 10
print('Aloha')

def name():
    print("I'm a quantummagician, and I love math.")

print('OK')
x = x+4
print(x)

# parameter is a variable in the function
def hello(word): #word=parameter
    if word == 'ed': #'ed'=argument
        print('Omg')
    elif word == 'es':
        print('I see')
    else:
        print('no worry')

hello('ed')
hello('es')
hello('xx')

# multiple parameters and arguments
def add(a,b):
    plus = a + b
    return plus # won't do anything
x = add(10,20)
print(x)

# compute gross salary
def gross(h,r):
    sal = h * r
    return sal
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h > 40:
    print((h-40)*r*0.5 + (h*r))
else:
    print(h*r)
    
