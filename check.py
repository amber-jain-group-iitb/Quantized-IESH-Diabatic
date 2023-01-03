import numpy as np

matrix=np.loadtxt("vib_dist_with_metal_4th_state.out")

for i in range(26):
	matrix[:,i]=matrix[:,i]*2.5

file2=open('result.out','w')
np.savetxt(file2,matrix)
file2.close()
