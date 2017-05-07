import socket
import cv2
import numpy
import datetime

from server import model


def rcv_all(sock, size):
    msg = b''
    while size:
        buf = sock.recv(size)
        if not buf:
            return None
        msg += buf
        size -= len(buf)
    return msg


def run(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', port))
    s.listen(True)
    while True:
        conn, addr = s.accept()
        print(addr, flush=True)

        # receive img , decode img , save img
        length = rcv_all(conn, 16)
        buf = rcv_all(conn, int(length))
        data = numpy.fromstring(buf, dtype='uint8')

        decoded_img=cv2.imdecode(data, 1)

        now = datetime.datetime.now()
        now_datetime = now.strftime('%y%m%d-%H%M%S%f')
        filename = 'img/{}.jpg'.format(now_datetime)
        cv2.imwrite(filename, decoded_img)

        # cv2.imshow('SERVER', decoded_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # model
        answer = model.temp_model(filename)

        # send answer to client
        conn.send(answer.encode())
        conn.close()


