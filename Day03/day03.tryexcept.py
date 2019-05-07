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