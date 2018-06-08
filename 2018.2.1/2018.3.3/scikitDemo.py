from scipy import io as spio
import numpy as np
a = np.ones((3,3))
spio.savemat('file.mat',{'a':a}) #保存字典到 file.mat
data = spio.loadmat('file.mat',struct_as_record=True)
print(data["a"])