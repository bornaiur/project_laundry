import cv2
import datetime
import os

def diffImage(i):
    diff0 = cv2.absdiff(i[0], i[1])
    diff1 = cv2.absdiff(i[1], i[2])
    return cv2.bitwise_and(diff0, diff1)


def updateCameraImage(cam, i, i_origin):
    i[0] = i[1]
    i[1] = i[2]

    i_origin[0] = i_origin[1]
    i_origin[1] = i_origin[2]

    ret, image = cam.read()

    if ret:
        i[2] = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        i_origin[2] = image
        return True
    else :
        return False


def run(source):
    os.system('sudo modprobe bcm2835-v4l2')

    ready = False
    thresh = 16
    #cam = cv2.VideoCapture(source)
    cam = cv2.VideoCapture(0)

    i = [None, None, None]
    i_origin = [None, None, None]

    for n in range(3):
        i_origin[n] = cam.read()[1]
        i[n] = cv2.cvtColor(i_origin[n], cv2.COLOR_RGB2GRAY)

    #init_scene = i[2]
    #cv2.imwrite('received_img/init.jpg', i_origin[2])

    wait_frame = 0

    while True:
        diff = diffImage(i)
        _, thrimg = cv2.threshold(diff, thresh, 1, cv2.THRESH_BINARY)
        count = cv2.countNonZero(thrimg)

        if count > 1:
            ready = True
            wait_frame = 0

        if ready and count < 1:
            wait_frame = wait_frame + 1
            
            #temp_diff = cv2.absdiff(init_scene, i[2])
            #_, temp_thrimg = cv2.threshold(temp_diff, thresh, 1, cv2.THRESH_BINARY)
            #count = cv2.countNonZero(temp_thrimg)

            if wait_frame > 15: #and count > 1:
                wait_frame = 0
                ready = False

                yield(i_origin[2])
                # now = datetime.datetime.now()
                # now_datetime = now.strftime('%y%m%d-%H%M%S%f')
                # cv2.imwrite('img/{}.jpg'.format(now_datetime), i_origin[2])

        # cv2.imshow('Detecting Motion', i_origin[2])
        if not updateCameraImage(cam, i, i_origin) :
            break
        # updateCameraImage(cam, i, i_origin)
        # key = cv2.waitKey(10)
        # if key == 27:
        #     break



