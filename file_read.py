'''
file_location = '/home/metal-machine/Desktop/nohup.out'
import re
import time
import numpy as np
a=np.array([])
with open(file_location,'r') as f:
    m = re.findall(r'tt\d\d\d\d\d\d\d',f.read())
    np_array = np.append(a,m)
    print np_array
    print np_array.size
    print 'unique'
    print np.unique(np_array)
    print np.unique(np_array).size
    np.save('/home/metal-machine/Desktop/nohup.npy',np.unique(np_array))    
'''
#file_location = '/home/arshpreetsingh/nohup.out'
file_location = '/home/metal-machine/Desktop/nohup.out'

def read_in_chunks(file_object):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read()
        if not data:
            break
        yield data
import numpy as np
import re
a=np.array([])
my_regex=re.compile(r'tt\d\d\d\d\d\d\d')
f = open(file_location)

def iterate_regex():
    for piece in read_in_chunks(f):
        yield re.findall(my_regex,piece)
for i in iterate_regex():
    np_array = np.append(a,i)
print np_array
print np_array.size
print 'unique'
print np.unique(np_array)
print np.unique(np_array).size

    #print m

'''
import re
import time
import numpy as np
a=np.array([])
my_regex = re.compile(r'tt\d\d\d\d\d\d\d')
with open(file_location,'r') as f:
    m = re.findall(my_regex,f.read())
    np_array = np.append(a,m)
    print np_array
    print np_array.size
    print 'unique'
    print np.unique(np_array)
    print np.unique(np_array).size
    #np.save('/home/arshpreetsingh/nohup.npy',np.unique(np_array))
'''
