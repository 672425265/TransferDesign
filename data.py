import h5py    
import numpy as np  

file_name = 'data/data.h5'

f = h5py.File(file_name, 'r') 

a_group_key = list(f.keys())[0]
print a_group_key
# Get the data
data = list(f[a_group_key])
print data

for i in f[a_group_key]['bandgap_1']:
	print i
