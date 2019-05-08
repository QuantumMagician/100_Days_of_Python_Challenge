# indefinite loops
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
        print('pardon?')
        continue
    elif x == 'done':
        break
print('Thank you')   


# definite loops
for i in [1,2,3,4,5]:
    print(i)
print('Thank you very much.')

# funny definite loops
friends = ['Rachel', 'Monica', 'Phoebe', 'Joey', 'Chandler', 'Ross']
for bf in friends:
    print('I love you:', bf)
print('I love you too.')


# finding the maximum value
max = -1
print('Max number so far is', max)
for num in [10, 100, -2, 74, 99, -100]:
    if num > max:
        max = num
    print(max, num)
print('After all, the max number is', max)


# finding min value
min = -1
print('Min number so far is', min)
for num in [10, 100, -2, 74, 99, -100]:
    if num < min:
        min = num
    print(min, num)
print('After all, min number so far is', min)


# None
# is/is not operator
min = None
print('Min number so far is', min)
for num in [10, 100, -2, 74, 99, -100]:
    if min is None:
        min = num
    elif num < min:
        min = num
    print(min, num)
print('After all, min number so far is', min)


# counting
count = 0
print('Before count is ', count)
for num in [10, 100, -2, 74, 99, -100]:
    count += 1
    print(count, num)
print('How many number in num? ', count)


# sum
total = 0
print('Before total is ', total)
for num in [10, 100, -2, 74, 99, -100]:
    total += num
    print(total, num)
print('What is total? ', total)

# avg
count = 0
total = 0
print('Before', count, total)
for num in [10, 100, -2, 74, 99, -100]:
    count += 1
    total += num
    avg = total/count
print('count is', count, 'total is', total, 'average is', avg)


# filtering
print('Before max number was')
for num in [10, 100, -2, 74, 99, -100]:
    if num > 50:
        print('Max number is', num)
print('Thanks.')


# boolean
x = False
print('Before x is', x)
for num in [10, 100, -2, 74, 99, -100]:
    if num == 100:
        x = True
    else:
        x = False
    print(x, num)


#
count = 0
total = 0.
while True:
    val= input('Enter a number: ')
    if val == 'abc':
        break
    try:
        fval= float(val)
        print(fval)
    except:
        print('Invalid input')
        continue
    count += 1
    total += fval

print('Good job')
print('total is', total, 'count is', count)