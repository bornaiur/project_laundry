import client_socket
import camera_detect
import time
import cv2

if __name__ == "__main__":
    image_detect = camera_detect.run()

    print(image_detect)
    print(type(image_detect))
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




