import cv2
import numpy as np
import time


def diffImage(i):
    diff0 = cv2.absdiff(i[0], i[1])
    diff1 = cv2.absdiff(i[1], i[2])
    return cv2.bitwise_and(diff0, diff1)

def updateCameraImage(cam, i):
    i[0] = i[1]
    i[1] = i[2]
    ret, image = cam.read()
    if ret:
        i[2] = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


if __name__ == "__main__":
    thresh = 32
    cam = cv2.VideoCapture('in.mp4')
    i = [None, None, None]
    init_scene = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    stopped_scene = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    for n in range(3):
        i[n] = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    index = 1;

    while True:
        diff = diffImage(i)
        ret, thrimg = cv2.threshold(diff, thresh, 1, cv2.THRESH_BINARY)
        count = cv2.countNonZero(thrimg)

        if (count < 1):
            diff_init = diffImage([init_scene, i[1], i[2]])
            _, thrimg_init = cv2.threshold(diff_init, thresh, 1, cv2.THRESH_BINARY)

            diff_stopped = diffImage([stopped_scene, i[1], i[2]])
            _, thrimg_stop = cv2.threshold(diff_stopped, thresh, 1, cv2.THRESH_BINARY)

            if (cv2.countNonZero(thrimg_init) > 1) and (cv2.countNonZero(thrimg_stop) > 1):
                now = time.localtime()
                s = "%02d-%02d-%02d-%d" % (now.tm_hour, now.tm_min, now.tm_sec, index)
                index = index + 1
                cv2.imwrite('img/{}.jpg'.format(s), i[2])

                stopped_scene = i[2]
        # if (count > 1):
        #     # nz = np.nonzero(thrimg)
        #     # cv2.rectangle(diff, (min(nz[1]), min(nz[0])), (max(nz[1]), max(nz[0])), (255, 0, 0), 2)
        #     # cv2.rectangle(i[0], (min(nz[1]), min(nz[0])), (max(nz[1]), max(nz[0])), (0, 0, 255), 2)
        #     now = time.localtime()
        #     s = "%02d-%02d-%02d-%d" % (now.tm_hour, now.tm_min, now.tm_sec, index)
        #     index = index+1
        #     cv2.imwrite('img/{}.jpg'.format(s), i[2])

        cv2.imshow('Detecting Motion', diff)
        updateCameraImage(cam, i)
        key = cv2.waitKey(10)
        if key == 27:
            break




