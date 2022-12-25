import cv2

def load_image():
    img = cv2.imread('data/makovska.png')
    cv2.imshow('Output', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    load_image()
