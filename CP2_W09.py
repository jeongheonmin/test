import numpy as np
import random

ary1_1 = np.random.randint(0,9,size=(1,10))
ary1_2 = np.random.randint(0,9,size=(1,10))
ary2_1 = np.random.randint(0,9,size=(3,3))
ary2_2 = np.random.randint(0,9,size=(3,3))

print(np.argmin(ary1_1))
print(np.argmin(ary2_1))

print(np.argmax(ary1_1))
print(np.argmax(ary2_1))

print(np.argsort(ary1_1))
print(np.argsort(ary2_1))

print(np.concatenate((ary1_1,ary1_2),axis=0))
print(np.concatenate((ary2_1, ary2_2),axis=1))

print(ary1_1)
print(ary1_2)


ary1_3 = ary1_1.reshape(2,5)

print(ary1_3)
ary2_3 = ary2_1.reshape(9)
print(ary2_3)

print(ary2_1.transpose(1,0))
print(ary1_1.transpose(1,0))