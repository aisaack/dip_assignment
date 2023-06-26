from cfg import berkeley
from utils import plot_all
import cv2 as cv


def reduce_contrast(img, thresh=3):
    clahe = cv.createCLAHE(clipLimit=thresh)
    contrast = clahe.apply(img)
    contrast = cv.cvtColor(contrast, cv.COLOR_GRAY2RGB)
    return contrast


def plot_q3():
    berkeley_gray = cv.cvtColor(berkeley, cv.COLOR_RGB2GRAY)
    contrast = reduce_contrast(berkeley_gray)
    bright = cv.addWeighted(contrast, 0.87, contrast, 0, 0)
    plot_all([berkeley, contrast, bright], labels=['Original', 'Adjust contrast', 'Adjust brightness'])