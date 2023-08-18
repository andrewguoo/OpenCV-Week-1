import cv2 as cv

def main():
    selfie = cv.imread("selfie.jpg")
    cv.imshow('Selfie', selfie)
    cv.waitKey(0)

if __name__ == "__main__":
    main()