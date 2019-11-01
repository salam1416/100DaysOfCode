# file handling

# opening file for appending
f = open('demofile.txt','a')

# writing in the file
f.write('what is your name?')

#closing the file
f.close()

# writing in a file

fp2 = open('demofile3.txt','w')
fp2.write('Now the file has more content!')

# open and read the file after the appending
fp2.write('what up')

fp2.close()



# check if file exist
if os.path.exists('demofile3.txt'):
    print('it exists')
else:
    print('it doesn not exist')
