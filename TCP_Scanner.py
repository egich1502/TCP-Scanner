import socket
import threading


def scan_port(ip, port, list):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connect = sock.connect_ex((ip, port))
        if connect == 0:
            list.append(port)
        sock.close()
        return port
    except:
        pass


if __name__ == '__main__':
    a = []
    ip = input('Enter ip: ')
    start = int(input('Enter starting port: '))
    end = int(input('Enter last port: '))

    for i in range(start, end + 1):
        thrd = threading.Thread(target=scan_port, args=(ip, i, a))
        thrd.start()

    if not a:
        print('No open ports')
    else:
        print('Opened ports: ', *a)
