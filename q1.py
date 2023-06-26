from cfg import cbs, label, ks
from utils import plot
import cv2 as cv


def prepare_img():
    gauss = [cv.GaussianBlur(img, (ks, ks), 1, 1) for img in cbs]
    mean = [cv.blur(img, (ks, ks)) for img in cbs]
    median = [cv.medianBlur(img, ks) for img in cbs]
    return gauss, mean, median
    

def plot_q1():
    gauss, mean, median = prepare_img()
    imgs = [img for img in zip(gauss, mean, median)]
    index = 4
    for i in range(index):
        plot(imgs[i], label, i+1, figsize=(7.5, 4.5))

# if __name__ == '__main__':
#     question()
#     answer_q1()
#     answer()