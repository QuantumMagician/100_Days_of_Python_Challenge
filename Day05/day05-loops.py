n = 10
while n > 0:
    print(n, "is bigger than o")
    n = n - 1 #otherwise, endless loop
print('Good job')
print("n is",0)

# break
while True:
    x = input('say something: ')
    if x == 'bye':
        break #until you got 'bye', it keeps looping.
    print(x)
print('I am done.')

# continue
while True:
    x = input('say something: ')
    if x[0] == '#':
        print('hashtag')
    elif x == '@':
        continue
    elif x == 'done':
        print(x)
 print('Thank you')   
        