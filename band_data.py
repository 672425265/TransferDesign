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
		print str(id) + ' A: w/o gap'

		if id % 5 == 0:
			output_file_name = 'data/band/testA/' + str(id) + '.png'
			plt.imsave(output_file_name, img, format="png", cmap="hot")
		else:
			output_file_name = 'data/band/trainA/' + str(id) + '.png'
			plt.imsave(output_file_name, img, format="png", cmap="hot")

		
	else:
		img = f[i]['epsilon_grid'][:]
		img = np.array(img).reshape([32, 32])

		print str(id) + ' B: w gap'

		if id % 5 == 0:
			output_file_name = 'data/band/testB/' + str(id) + '.png'
			plt.imsave(output_file_name, img, format="png", cmap="hot")
		else:
			output_file_name = 'data/band/trainB/' + str(id) + '.png'
			plt.imsave(output_file_name, img, format="png", cmap="hot")


	id += 1
	plt.clf()

