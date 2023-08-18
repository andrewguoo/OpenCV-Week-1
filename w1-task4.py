import cv2 as cv
import matplotlib.pyplot as plt

def main():
    selfie = cv.cvtColor(cv.imread("selfie.jpg"), cv.COLOR_BGR2RGB)
    plt.imshow(selfie)
    plt.title("Selfie")
    plt.xlabel("yes")
    plt.ylabel("no")
    plt.show()

if __name__ == "__main__":
    main()