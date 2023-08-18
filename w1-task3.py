import cv2 as cv

def rescale(frame: cv.Mat, scale:float) -> cv.Mat:

  height =int(frame.shape[0] * scale)

  width =int(frame.shape[1] * scale)

  dim = (width, height)

  return cv.resize(frame, dim, interpolation=cv.INTER_AREA)
                   
def main():
    selfie = cv.imread("selfie.jpg")
    rescaled_selfie = rescale(selfie, 0.1)
    cv.imshow('Selfie', rescaled_selfie)
    cv.waitKey(0)

if __name__ == "__main__":
    main()