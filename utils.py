import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from cfg import coins

def plot(cbs, label=None, idx=None, figsize=(12, 7)):
    
    if label:
        fig = plt.figure(figsize=figsize)
        axs = fig.subplots(1, len(label))
    else:
        fig = plt.figure(figsize=figsize)
        axs = fig.subplots(1, len(cbs))
    for i, img in enumerate(cbs):
        axs[i].imshow(cbs[i])
        axs[i].get_xaxis().set_ticks([])
        axs[i].get_yaxis().set_ticks([])
        if label:
            axs[i].set_xlabel(f'{label[i]} on cb{idx}')
        else:
            axs[i].set_xlabel(f'cb{i+1}')
    fig.tight_layout()


def plot_all(imgs, figsize=(16, 9), labels=None, vertical=False, gray=False):
    assert len(imgs) == len(labels)
    fig = plt.figure(figsize=figsize)
    if vertical is True:
        axs = fig.subplots(len(imgs), 1)
    else:
        axs = fig.subplots(1, len(imgs))
    for i in range(len(imgs)):
        if gray is True:
            axs[i].imshow(imgs[i], cmap='gray')
        else:
            axs[i].imshow(imgs[i])
        axs[i].get_xaxis().set_ticks([])
        axs[i].get_yaxis().set_ticks([])
        axs[i].set_xlabel(labels[i])
    fig.tight_layout()


def plot_one(img, figsize=(16, 9), gray=True, label=None):
    fig = plt.figure(figsize=figsize)
    axs = fig.subplots(1, 1)
    if gray is True:
        axs.imshow(img, cmap='gray')
    elif gray is False:
        axs.imshow(img)
    axs.get_xaxis().set_ticks([])
    axs.get_yaxis().set_ticks([])
    axs.set_xlabel(label)
    fig.tight_layout()


def edge_detection(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    gx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3)
    gy = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=3)

    abs_gx = cv.convertScaleAbs(gx)
    abs_gy = cv.convertScaleAbs(gy)

    edge = cv.addWeighted(abs_gx, 0.4, abs_gy, 0.4, 0)

    return img, gray, gx, gy, abs_gx, abs_gy, edge

def external_boundary(edge):
    _, thresh = cv.threshold(edge, 100, 255, cv.THRESH_BINARY)
    circles = cv.HoughCircles(
        thresh, cv.HOUGH_GRADIENT, dp=1.2118, minDist=20, param1=50, param2=30, minRadius=10, maxRadius=26)
    if circles is None:
        print('No cirsles detected')
    else:
        circles = np.uint16(np.around(circles))

    circles = circles.squeeze(0)
    # print(circles.shape)
    # print(circles[:5])

    contour = coins.copy()
    for i in circles:
        # print(i)
        # break
        # draw the outer circle
        centre = (i[0], i[1])
        rad = i[2]
        cv.circle(contour, centre, rad, (0, 255, 0), 2)

    return thresh, contour


def failure_case(edge):
    _, sobel_thrsh = cv.threshold(edge, 100, 255, cv.THRESH_BINARY)
    contour_sobel, _ = cv.findContours(sobel_thrsh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    sobel_res = coins.copy()
    cv.drawContours(sobel_res, contour_sobel, -1, (0, 255, 0), 2)
    return sobel_res
