import h5py    
import numpy as np  
import matplotlib.pyplot as plt


file_name = 'data/data.h5'

f = h5py.File(file_name, 'r') 


A = []
B = []
id = 0

for i in f.keys():
	if f[i]['bandgap_1'][0] == 0:
		img = f[i]['epsilon_grid'][:]
		img = np.array(img).reshape([32, 32])
		plt.imshow(img)
		print str(id) + ' A: w/o gap'
		output_file_name = 'data/band/trainA/' + str(id) + '.jpg'
		plt.savefig(output_file_name, format='jpg')
	else:
		img = f[i]['epsilon_grid'][:]
		img = np.array(img).reshape([32, 32])
		plt.imshow(img)
		print str(id) + ' B: w gap'
		output_file_name = 'data/band/trainB/' + str(id) + '.jpg'
		plt.savefig(output_file_name, format='jpg')
	id += 1
	plt.clf()

