import numpy as np

#int_list = list(range(10))

#int_arr = np.array(int_list)

#print("int_arr ndim: ", int_arr.ndim)
#print("int_arr shape: ", int_arr.shape)
#print("int_arr size: ", int_arr.size)
#print("int_arr dtype: ", int_arr.dtype)

#print(int_arr[2:6])
#print(int_arr[:6])
#print(int_arr[2:])
#print(int_arr[::3])
#print(int_arr[::-1])

#arr_2d=np.zeros((3,7))
#print(arr_2d)
#arr_2d=np.zeros((3,2,4))
#print(arr_2d)

#arr_uint_3d= np.ones((3,2,4),dtype=np.uint8)

#print(arr_uint_3d)
#arr_float_3d[0,:,:]


#from sklearn import datasets
#mnist= datasets.fetch_mldata('MNIST original')

#print(mnist.data.shape)
#print(mnist.target.shape)
#print(np.unique(mnist.target))

#import matplotlib as mpl
#import matplotlib.pyplot as plt


#import numpy as np
#x = np.linspace(0, 10, 100)

#plt.plot(x,np.sin(x))
#plt.show()

import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()
#print(digits.data.shape)
#print(digits.images.shape)
#img = digits.images[1, :, :]
#plt.imshow(img, cmap='gray')
#plt.show()

for image_index in range(10):
# images are 0-indexed, but subplots are 1-indexed
    subplot_index = image_index + 1
    plt.subplot(2, 5, subplot_index)
    plt.imshow(digits.images[image_index, :, :], cmap='gray')
    plt.show()

