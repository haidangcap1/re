import npu

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
import os
' && '.join([f'export {name}="{value}"' for name, value in os.environ.items()])
#@title **Mod GPU**

from numba import jit, cuda
import numpy as np
# to measure exec time
from timeit import default_timer as timer

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

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import mixed_precision

mixed_precision.set_global_policy('mixed_float16')
#@title HIDUP INDAH BILA MENCARI BERKAH

