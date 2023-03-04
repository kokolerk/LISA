# import tkinter
import torch
import os
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('TkAgg')
path="../data/CMNIST/ColoredMNIST"
data=torch.load(os.path.join(path, "test.pt"))

a=0
b=0
c=0
d=0

for idx,sample in enumerate(data):
    img= sample[0]
    label= sample[1]
    col= sample[2]
    if label==0 and col==True:
        a=a+1
    elif label==0 and col==False:
        b=b+1
    elif label==1 and col==True:
        c=c+1
    else :
        d=d+1
    
        # print("label:",label)
        # print("color:",col)
        # fig, ax = plt.subplots()
        # ax.imshow(img)
        # plt.savefig(str(label)+'_'+str(col))
        # break

print(a,b,c,d)

'''
0-4,red;0-4,green;5-9,red;5-9,green
train 12130 2998 3091 11781
val 2465 2591 2431 2513
test 1068 8966 8953 1013

green colored_minist 0 False
red colored_minist 1 True 
0-4 red2green2 0
5-9 red2green2 1

Training Data...
    colored_minist = 0, red2green2 = 0: n = 2998  0-4,green blue
    colored_minist = 0, red2green2 = 1: n = 11781 5-9,green blue
    colored_minist = 1, red2green2 = 0: n = 12130 0-4,red purple
    colored_minist = 1, red2green2 = 1: n = 3091  5-9,red purple
Validation Data...
    colored_minist = 0, red2green2 = 0: n = 2591
    colored_minist = 0, red2green2 = 1: n = 2513
    colored_minist = 1, red2green2 = 0: n = 2465
    colored_minist = 1, red2green2 = 1: n = 2431
Test Data...
    colored_minist = 0, red2green2 = 0: n = 8966
    colored_minist = 0, red2green2 = 1: n = 1013
    colored_minist = 1, red2green2 = 0: n = 1068
    colored_minist = 1, red2green2 = 1: n = 8953

5,green。
5-9 label: 1
green color: False
'''   
    
