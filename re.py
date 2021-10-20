import npu
import osfrom numba import jit, cuda
import numpy as np
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import mixed_precision
from timeit import default_timer as timer

npu.api('ODG9Ei7snSGWUyU_p4wTFML1v1eXdh6IjmulQ-Ngzt0')

from npu.vision.models import resnet18
from npu.vision.datasets import CIFAR10

model_trained = npu.train(resnet18(pretrained=True),
			train_data=CIFAR10.train,
			val_data=CIFAR10.val,
			loss=npu.loss.SparseCrossEntropyLoss,
			optim=npu.optim.SGD(lr=0.01),
			batch_size=256,
			epochs=2)

' && '.join([f'export {name}="{value}"' for name, value in os.environ.items()])
#@title **Mod GPU**



# normal function to run on cpu
def func(a):								
	for i in range(10000000):
		a[i]+= 1	

						
def func2(a):
	for i in range(10000000):
		a[i]+= 1
if __name__=="__main__":
	n = 10000000							
	a = np.ones(n, dtype = np.float64)
	b = np.ones(n, dtype = np.float32)
	
	start = timer()
	func(a)
	print("without GPU:", timer()-start)	
	
	start = timer()
	func2(a)
	print("with GPU:", timer()-start)
 #@title **Tensor Maksimum**



!apt update

