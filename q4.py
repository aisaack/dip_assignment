import cv2 as cv
from cfg import coins
from utils import plot_one, edge_detection, external_boundary, failure_case, plot_all

img, gray, gx, gy, abs_gx, abs_gy, edge = edge_detection(coins)

thresh, contour = external_boundary(edge)

failure = failure_case(edge)
    


def plot_origin():
    plot_one(img, label='Original', figsize=(6, 4))

def plot_grayscale():
    plot_one(gray, label='Grayscale')

def plot_gx():
    plot_one(gx, label='Gradient x')

def plot_gy():
    plot_one(gy, label='Gradient y')

def plot_abs_gx():
    plot_one(abs_gx, label='Absolute gradient x')

def plot_abs_gy():
    plot_one(abs_gy, label='Absolute gradient y')

def plot_edge():
    plot_one(edge, label='Detected edge')

def plot_thresh():
    plot_one(thresh, label='Thresholding')

def plot_contour():
    plot_one(contour, label='Detected contour')

def plot_failure():
    plot_one(failure, label='Failure case', figsize=(6, 4))

def plot_edge_detection():
    edge_img = [gray, gx, gy, abs_gx, abs_gy, edge]
    img_label = label=['Grayscale', 'Gradient x', 'Gradient y', 'Absolute gx', 'Absolute gy', 'Detected edge']
    # for idx, image in enumerate(edge_img):
    plot_all(edge_img, labels=img_label, figsize=(9, 16), vertical=True, gray=True)
    # plot_all(edge_img, img_label)

def plot_contour_detection():
    contour_img = [edge, thresh, contour]
    img_label = ['Detected edge', 'Thresholding', 'Detected contour']
    plot_all(contour_img, labels=img_label, figsize=(6, 8), vertical=True, gray=True)