# Python Try-Except
try:
    print('a')
except NameError: # if this specific exception occured
    print('a name-error exception occured')
except: # another exception occured
    print('another exception occured')
else: # will print when no error is catched
    print('no exceptions! ')
finally: #will happend regardless if there's exception or not
    print('anyway ')