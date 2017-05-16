import time
import cv2
import sys

from rasp import camera_detect
from rasp import client_socket

if __name__ == "__main__":
    #image_detect = camera_detect.run(sys.argv[1])
    image_detect = camera_detect.run(None)

    index = 1
    try:
        while True:
            img = next(image_detect)
            print('{}> image detected'.format(index), flush=True)
            cv2.imshow('{}> Detecting Image'.format(index), img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            print('{}> send img to server....'.format(index), flush=True)
            label = client_socket.run('127.0.0.1', 9000, img)
            print('{}> received label...'.format(index), flush=True)
            print('{}> label = {}'.format(index, label))
            print('-------------------------------', flush=True)
            time.sleep(1)
            index = index + 1
    except StopIteration:
        pass
    finally:
        del image_detect




