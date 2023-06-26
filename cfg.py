import cv2 as cv

ks = 5
cbs = [cv.imread(f'./Images/cb{i}.tif') for i in range(1, 5)]
label = ['Gaussian filter', 'Mean filter', 'Median filter']
sigma = ['sigma 0.25', 'sigma 1', 'sigma 4', 'sigma 8']

berkeley = cv.imread(f'./Images/Berkeley.jpg')

coins = cv.imread(f'./Images/coins.jpg')