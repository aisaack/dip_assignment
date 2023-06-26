from cfg import cbs, sigma, ks
from utils import plot
import cv2 as cv

def prepare_img():
    sigma_01 = [cv.GaussianBlur(img, (ks, ks), sigmaX=0.25, sigmaY=0.25) for img in cbs]
    sigma_1 = [cv.GaussianBlur(img, (ks, ks), sigmaX=1, sigmaY=1) for img in cbs]
    sigma_4 = [cv.GaussianBlur(img, (ks, ks), sigmaX=4, sigmaY=4) for img in cbs]
    sigma_8 = [cv.GaussianBlur(img, (ks, ks), sigmaX=8, sigmaY=8) for img in cbs]
    # sigma_16 = [cv.GaussianBlur(img, (ks, ks), sigmaX=16, sigmaY=16) for img in cbs]
    sigma_all = [img for img in zip(sigma_01, sigma_1, sigma_4, sigma_8)]
    return sigma_all



def plot_q2():
    idx = 4
    sigma_all = prepare_img()
    for i in range(idx):
        plot(sigma_all[i], sigma, i+1, (13, 8))


# if __name__ == '__main__':
#     img = prepare_img()
#     print(len(img[1]))