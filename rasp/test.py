import cv2
import time



if __name__ == "__main__":
    cam = cv2.VideoCapture('timer.mp4')
    index = 1

    i = None
    while True:
        ret, image = cam.read()
        if ret:

            cv2.imwrite('{}.jpg'.format(index), cv2.cvtColor(image, cv2.COLOR_RGB2GRAY))
            index = index + 1
        time.sleep(3)
        key = cv2.waitKey(10)
        if key == 27:
            break



