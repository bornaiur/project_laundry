import socket
import cv2
import numpy


def conn(s_ip, s_port):
    sock = socket.socket()
    sock.connect((s_ip, s_port))
    return sock


def send(sock, image):
    # encoding
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    result, img = cv2.imencode('.jpg', image, encode_param)
    data = numpy.array(img)
    img_to_str = data.tostring()

    # send img
    sock.send(str(len(img_to_str)).ljust(16).encode())
    sock.send(img_to_str)

    # receive answer from server
    received = sock.recv(1024).decode()

    sock.close()

    return received


def run(ip, port, img):
    s = conn(ip, port)
    ans = send(s, img)
    return ans


# for test
if __name__ == "__main__":
    print(run('127.0.0.1', 9000, cv2.VideoCapture('in.mp4').read()[1]))